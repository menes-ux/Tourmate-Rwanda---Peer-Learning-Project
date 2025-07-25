from models.tour_guide import TourGuide
from db import SessionLocal


def register_tour_guide():
    """
    This is a function that asks a user to register as a tour guide with their full name, email, and country
    """
    session = SessionLocal()
    try:
        print("Register New Tour Guide")
        fullname = input("Full Name: ").strip()
        email = input("Email: ").strip()
        country = input("Country: ").strip()
        if fullname and email and country:
            tour_guide = TourGuide.create_tour_guide(fullname, email, country)
            session.add(tour_guide)
            session.commit()
        else:
            print("\n All fields are required. Tour Guide was not created.")

        session.refresh(tour_guide)

        print("\nTour Guide Registered Successfully!")
        print(tour_guide)
    except Exception as e:
        session.rollback()
        print("Error registering tour guide:", e)
    finally:
        session.close()