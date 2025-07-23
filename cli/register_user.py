from models.user import User
from db import SessionLocal

def register_user():
    session = SessionLocal()
    try:
        print(" Register New User")
        fullname = input("Full Name: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        country = input("Country: ").strip()

        if fullname and email and password and country:
            user = User.create_user(fullname, email, password, country)
            session.add(user)
            session.commit()
            session.refresh(user)
            print("\n Your account has been created successfully!")
            print(user)
        else:
            print("\n All fields are required. User was not created.")
    except Exception as e:
        session.rollback()
        print("Error creating user:", e)
    finally:
        session.close()
