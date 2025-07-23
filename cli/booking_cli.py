from models.bookings import Booking
from db import SessionLocal

def create_booking():
    try:
        group_size = input("Enter group size: ")
        visting_date = input("Enter visiting date (YYYY-MM-DD HH:MM:SS): ")
        price = input("Enter price: ")
        tour_guide_id = input("Enter tour guide ID: ")
        user_id = input("Enter user ID: ")
        cab_id = input("Enter cab ID: ")

        booking = Booking(
            group_size=group_size,
            visting_date=visting_date,
            price=price,
            tour_guide_id=tour_guide_id,
            user_id=user_id,
            cab_id=cab_id
        )

        db = SessionLocal()
        db.add(booking)
        db.commit()
        db.refresh(booking)

        print(f"Booking created successfully: {booking}")
    except Exception as e:
        print(f"Error creating booking: {e}")
    finally:
        db.close()
        

def book_tour_menu():
    while True:
        print("\nBooking Options:")
        print("1: New Booking")
        print("2: View Booking")
        print("3: Complete Booking")
        print("4: Back to Main Menu")

        sub_choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        match sub_choice:
            case "1":
                print("You selected: New Booking")
                create_booking()
            case "2":
                print("You selected: View Booking")
                # Add logic here
            case "3":
                print("You selected: Complete Booking")
                # Add logic here
            case "4":
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
