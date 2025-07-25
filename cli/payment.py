from models.bookings import Booking
from db import SessionLocal

session = SessionLocal()

def payment_flow(session, booking_reference: str):
    """
    This is a function that simulates the payment flow for a booking.
    """
    booking = session.query(Booking).filter_by(booking_reference=booking_reference).first()

    if not booking:
        print("No Booking found with that reference Code.")
        return

    if booking.confirmed:
        print("Booking is already confirmed.")
        return

    if booking.confirmed is False:
        print(f"Processing Payment for {booking.booking_reference}...")
        booking.confirmed = True
        session.commit()

    print(f"Payment for {booking.booking_reference} processed successfully. Booking confirmed.")
    print("-" * 40)

def paymentPrompt(session):
    """
    This is a function that prompts the user to pay for their booking.
    """
    inputValue = input("Do you want to pay now? (yes/no): ").strip().lower()
    
    if inputValue != "yes":
        print("Payment canceled.")
        return

    booking_ref = input("Please enter your Booking Reference: ").strip().upper()

    if not booking_ref:
        print("Booking reference cannot be empty.")
        return

    payment_flow(session, booking_ref)