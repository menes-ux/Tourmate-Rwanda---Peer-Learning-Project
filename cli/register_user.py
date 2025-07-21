from models.user import User
from db import SessionLocal

def register_user():
    session = SessionLocal()
    try:
        print("👤 Register New User")
        fullname = input("Full Name: ")
        email = input("Email: ")
        password = input("Password: ")
        country = input("Country: ")

        user = User.create_user(fullname, email, password, country)
        session.add(user)
        session.commit()
        session.refresh(user)

        print("\n✅ Account Created Successfully!")
        print(user)
    except Exception as e:
        session.rollback()
        print("Error creating user:", e)
    finally:
        session.close()
