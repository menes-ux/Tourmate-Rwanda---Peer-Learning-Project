from  models.cab import Cab
from db import SessionLocal

def register_cab():
    try:
        cab_number = input("Enter cab number: ")
        driver_name = input("Enter driver name: ")
        driver_contact = input("Enter driver contact: ")

        cab = Cab.create_cab(cab_number, driver_name, driver_contact)

        db = SessionLocal()
        db.add(cab)
        db.commit()
        db.refresh(cab)

        print(f"Registered new cab: {cab}")
    except Exception as e:
        print(f"Error registering cab: {e}")
    finally:
        db.close()
