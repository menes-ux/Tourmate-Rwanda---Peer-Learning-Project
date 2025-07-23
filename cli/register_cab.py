from  models.cab import Cab
from db import SessionLocal

def register_cab():
    try:
        cab_number = input("Enter cab number: ").strip()
        driver_name = input("Enter driver name: ").strip()
        driver_contact = input("Enter driver contact: ").strip()

        if cab_number and driver_name and driver_contact:
            cab = Cab.create_cab(cab_number, driver_name, driver_contact)
            db = SessionLocal()
            db.add(cab)
            db.commit()
            db.refresh(cab)
            print(f"Registered new cab: {cab}")
        else:
            print("\n All fields are required. Cab was not created.")
    except Exception as e:
        print(f"Error registering cab: {e}")
    finally:
        db.close()