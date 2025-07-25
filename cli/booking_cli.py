from sqlalchemy.sql import func
from models.tourist_site import TouristSite
from models.bookings import Booking, handle_grouping, get_user_group
from db import SessionLocal
import random
import string
from datetime import datetime
from cli.register_user import login_user, register_user
from cli.payment import paymentPrompt
    
session = SessionLocal()

def book_tour_flow(user_id):
    try:
        site_code = input("Enter Site Code to Visit: ").strip()
        tourist_site = session.query(TouristSite).filter_by(site_code=site_code).first()

        if not tourist_site:
            print("You entered an invalid Site Code.")
            return

        print(f"\nYou selected: {tourist_site.sitename} ({tourist_site.location})")

        group_size = int(input("How many people are you booking for? "))

        if group_size < 1 or group_size > 4:
            print("Group size must be between 1 and 4.")
            return

        while True:
            date_str = input("Enter visit date (YYYY-MM-DD): ").strip()
            try:
                visit_date = datetime.strptime(date_str, "%Y-%m-%d")
                if Booking.is_valid_weekend_date(visit_date):
                    break
                else:
                    print("Only Friday, Saturday, or Sunday are allowed. Please try again.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        def generateRandomBookingReference(length=6):
            prefix = "BOOK-"
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            return prefix + code

        booking = Booking(
            booking_reference=generateRandomBookingReference(),
            group_size=group_size,
            visting_date=visit_date,
            price=tourist_site.gatepassfee,
            user_id=user_id,
            tour_guide_id=None, 
            cab_id=None,    
            tourist_site_id=tourist_site.id,
        )

        session.add(booking)
        session.commit()
        session.refresh(booking)

        print("\n🅱 Booking saved successfully.")
        print(f"Booking Reference: {booking.booking_reference}")
        print(f"Site: {tourist_site.sitename}")
        print(f"📅 Visit Date: {visit_date.strftime('%Y-%m-%d')}")
        print(f"Price: {tourist_site.gatepassfee} RWF")
        print(f"Group Size: {booking.group_size}")
        
        print("\nℹ️ Waiting to be grouped with others...")

        # Attempt grouping by site and date
        handle_grouping(session, visit_date, tourist_site.id)
        
        # Handle Payment
        paymentPrompt(session)
        print()
        
        # print_group_summary(session, tourist_site.id, visit_date)
        
        # Get user group details
        get_user_group(session, user_id, tourist_site.id, visit_date)

    except Exception as e:
        session.rollback()
        print("Error during booking:", e)
    finally:
        session.close()

def book_tour_menu():
    try:
        while True:
            print("\nBooking Options:")
            print("1: New Booking (Login Required)")
            print("2: View Booking")
            print("3: Complete Booking")
            print("4: Back to Main Menu")

            sub_choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

            match sub_choice:
                case "1":
                    print("\nYou selected: New Booking")
                    print("Please login to continue.\n")

                    user = None
                    while not user:
                        user = login_user()
                        if not user:
                            choice = input("Do you want to register? (y/n): ").lower()
                            if choice == 'y':
                                register_user()
                            else:
                                return

                    book_tour_flow(user.id)

                case "2":
                    print("You selected: View Booking")
                    # print_group_summary(session, tourist_site.id, visit_date)
                    user_email = input("Enter your email to view your booking: ").strip()
                    tourist_site = session.query(TouristSite).filter_by(site_code=input("Enter Site Code: ").strip()).first()
                    visit_date = input("Enter visit date (YYYY-MM-DD): ").strip()
                    if not tourist_site or not visit_date or not user_email:
                        print("Invalid site code, date, or email.")
                        continue
                    get_user_group(session, user_email, tourist_site, visit_date)
                case "3":
                    print("You selected: Complete Booking")
                    paymentPrompt(session)
                case "4":
                    print("Returning to Main Menu...")
                    break
                case _:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:    
        session.close()