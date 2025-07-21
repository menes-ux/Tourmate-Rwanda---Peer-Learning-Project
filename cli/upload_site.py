from models.tourist_site import Site
from db import SessionLocal


def register_newsite():
    session = SessionLocal()
    try:
        print("Register New Site")
        sitename = input("Site Name: ")
        location = input("Location: ")
        gatepass = input("Gatepass: ")

        user = Site.create_touristsite(sitename, location, gatepass,)
        session.add(user)
        session.commit()
        session.refresh(user)

        print("\n✅ Site Added Successfully!")
        print(user)
    except Exception as e:
        session.rollback()
        print("Error Adding New Site:", e)
    finally:
        session.close()