from db import Base, engine
from asciitext import welcome_message
from cli.upload_site import register_newsite, view_all_sites
from cli.register_cab import register_cab
from cli.register_tour_guide import register_tour_guide
from asciitext import all_sites


Base.metadata.create_all(bind=engine)


def main():
    print(welcome_message)
    
    while True:
        print()
        print("What do you want to do today?")
        print("1: View All Tourist Sites")
        print("2: Register as a Tour Guide")
        print("3: Book a Tour")
        print("4: Transactions")
        print("5: Add New Site (Admin)")
        print("6: Add New Cab (Admin)")
        print("7: Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, or 7): ").strip()

        match choice:
            case "1":
                print()
                print(all_sites)
                print("You selected: View All Tourist Sites")
                view_all_sites()
            case "2":
                print("You selected: Register as a Tour Guide")
                register_tour_guide()
            case "3":
                print("You selected: Book a Tour")
                # Add logic here
            case "4":
                print("You selected: Transactions")
                # Add logic here
            case "5":
                print("Admin Selected Add New Site")
                register_newsite()
            case "6":
                print("Admin Selected Add New Cab")
                register_cab()
            case "7":
                print("Exiting the application. Goodbye!")
                return
            case _:
                print("Invalid input. Please enter 1, 2, 3, 4, 5, 6, or 7.")


if __name__ == "__main__":
    main()
