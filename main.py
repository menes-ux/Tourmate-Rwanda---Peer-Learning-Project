from db import Base, engine
from asciitext import welcome_message
from cli.upload_site import register_newsite


Base.metadata.create_all(bind=engine)


def main():
    while True:
        print(welcome_message)

        print()
        print("What do you want to do today?")
        print("1: View All Tourist Sites")
        print("2: Register as a Tour Guide")
        print("3: Book a Tour")
        print("4: Transactions")
        print("5: Add New Site (Admin)")
        print("6: Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ").strip()

        match choice:
            case "1":
                print("You selected: View All Tourist Sites")
                # Add logic here
            case "2":
                print("You selected: Register as a Tour Guide")
                from cli.register_user import register_user
                register_user()
            case "3":
                print("You selected: Book a Tour")
                book_tour_menu()
            case "4":
                print("You selected: Transactions")
                # Add logic here
            case "5":
                print("Admin Selected Add New Site")
                register_newsite()
                
            case "6":
                print("Exiting the application. Goodbye!")
                return
            case _:
                print("Invalid input. Please enter 1, 2, 3, 4, 5, or 6.")


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
                # Add logic here
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


if __name__ == "__main__":
    main()
