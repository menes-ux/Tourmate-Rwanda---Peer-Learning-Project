from models.tourist_site import TouristSite
from db import SessionLocal
from asciitext import not_found


def register_newsite():
    session = SessionLocal()
    try:
        print("Register New Tourist Site")
        sitename = input("Tourist Site Name: ").strip()
        location = input("Location: ").strip()
        gatepassfee = input("Gatepass Fee: ").strip()

        if sitename and location and gatepassfee:
            siteData = TouristSite.create_touristsite(sitename, location, gatepassfee)
            session.add(siteData)
            session.commit()
            session.refresh(siteData)
            print("\nTourist Site Added Successfully!")
            print(siteData)
        else:
            print("\nAll fields are required. Tourist Site was not added.")
    except Exception as e:
        session.rollback()
        print("Error Adding New Tourist Site:", e)
    finally:
        session.close()

        
def view_all_sites():
    session = SessionLocal()
    try:
        sites = session.query(TouristSite).all()
        if not sites:
            print(not_found)
            return
        for site in sites:
            print(site)
    except Exception as e:
        print("Error retrieving tourist sites:", e)
    finally:
        session.close()