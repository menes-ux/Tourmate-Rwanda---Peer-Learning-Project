from models.user import User
from db import SessionLocal

session = SessionLocal()


def register_user():
    """
    This is a function that registers a new user in the system.
    """
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
        
        
def login_user():
    """
        This is a function that prompts the user to log in with their email and password
    """
    try:
        print("Login To Your Account")
        print("Please enter your email and password to log in.")
        print()
        
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        user = session.query(User).filter_by(email=email, password=password).first()
        if user:
            print(f"Thank you for logging in, {user.fullname}!")
            return user
        else:
            print("Check your email and password. User not found.")
            return None
    finally:
        session.close()
