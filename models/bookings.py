from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Integer, cast, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from datetime import datetime
import uuid
from db import Base  
from models.tour_guide import TourGuide
from models.group import Group
from models.cab import Cab



class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_size = Column(Integer, nullable=False)
    visting_date = Column(DateTime, nullable=False)
    price = Column(String, nullable=False)
    booking_reference = Column(String(20), unique=True, index=True, nullable=False)
    confirmed = Column(Boolean, default=False)

    tour_guide_id = Column(UUID(as_uuid=True), ForeignKey('tour_guides.id'), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    cab_id = Column(UUID(as_uuid=True), ForeignKey('cabs.id'), nullable=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey('groups.id'), nullable=True)
    tourist_site_id = Column(UUID(as_uuid=True), ForeignKey('tourist_sites.id'), nullable=False)

    user = relationship("User", back_populates="bookings")
    cab = relationship("Cab", back_populates="bookings")
    tour_guide = relationship("TourGuide", back_populates="bookings")
    group = relationship("Group", back_populates="bookings")
    tourist_sites = relationship("TouristSite", back_populates="bookings")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
       
    

    @classmethod
    def create(cls, group_size, visting_date, price, user_id, tourist_site_id, confirmed=False):
        return cls(
            booking_reference="",
            group_size=group_size,
            visting_date=visting_date,
            price=price,
            user_id=user_id,
            tourist_site_id=tourist_site_id,
            confirmed=False
        )

    def add_to_group(self, group_size, tour_guide_id, cab_id):
        self.group_size = group_size
        self.tour_guide_id = tour_guide_id
        self.cab_id = cab_id

    @staticmethod
    def is_valid_weekend_date(date_obj):
        return date_obj.weekday() in (4, 5, 6) 

    def __repr__(self):
        return (f"BookingId='{self.id}'\n"
                f"group_size='{self.group_size}'\n"
                f"visting_date='{self.visting_date}'\n"
                f"booking_reference='{self.booking_reference}'\n"
                f"price='{self.price}'\n"
                f"confirmed='{self.confirmed}'\n"
                f"tour_guide_id='{self.tour_guide_id}'\n"
                f"user_id='{self.user_id}'\n"
                f"cab_id='{self.cab_id}'")




GROUP_LIMIT = 4 

def handle_grouping(session, visiting_date, site_id):
    dateOfVisit = visiting_date.date()

    # Get all unconfirmed bookings for the given site and date
    unconfirmed_bookings = session.query(Booking).filter(
        cast(Booking.visting_date, Date) == dateOfVisit,
        Booking.tourist_site_id == site_id,
        Booking.confirmed == False
    ).order_by(Booking.created_at).all()

    if not unconfirmed_bookings:
        print("No unconfirmed bookings to group.")
        return

    for booking in unconfirmed_bookings:
        # Step 1: Check for existing groups
        existing_groups = (
            session.query(Group)
            .filter(
                cast(Group.visiting_date, Date) == dateOfVisit,
                Group.bookings.any(Booking.tourist_site_id == site_id)
            )
            .all()
        )

        selected_group = None

        for group in existing_groups:
            group_bookings = [b for b in group.bookings if b.tourist_site_id == site_id]
            current_size = sum(b.group_size for b in group_bookings)
            if current_size + booking.group_size <= GROUP_LIMIT:
                selected_group = group
                break

        # Step 2: If no suitable group, create one
        if not selected_group:
            tour_guide = session.query(TourGuide).order_by(func.random()).first()
            cab = session.query(Cab).order_by(func.random()).first()

            if not tour_guide or not cab:
                print("No Tour guide or Cab available.")
                return

            selected_group = Group(
                visiting_date=visiting_date,
                tour_guide_id=tour_guide.id,
                cab_id=cab.id
            )
            session.add(selected_group)
            session.commit()

        # Step 3: Assign booking to the group
        booking.group_id = selected_group.id
        booking.tour_guide_id = selected_group.tour_guide_id
        booking.cab_id = selected_group.cab_id
        booking.confirmed = False

        session.add(booking)
        session.commit()

        print(f"Booking {booking.booking_reference} assigned to Group {selected_group.id}")

    print(f"\nGrouping complete for site_id {site_id} on {dateOfVisit}")
    
    
    
def print_group_summary(session, site_id, visit_date):
    """
    Print group details (size, tour guide, cab) for a specific site and visit date.
    """

    dateOfVisit = visit_date.date()

    print(f"\n📋 Group Summary for site_id={site_id} on {dateOfVisit}:\n")

    groups = (
        session.query(Group)
        .filter(
            cast(Group.visiting_date, Date) == dateOfVisit,
            Group.bookings.any(Booking.tourist_site_id == site_id)
        )
        .all()
    )

    if not groups:
        print("No groups found.")
        return

    for group in groups:
        group_bookings = [b for b in group.bookings if b.tourist_site_id == site_id]
        group_size = sum(b.group_size for b in group_bookings)

        print(f"Group ID: {group.id}")
        print(f"Total People: {group_size}")
        print(f"Tour Guide: {group.tour_guide.fullname if group.tour_guide else 'Not assigned'}")
        print(f"Cab Driver: {group.cab.driver_name if group.cab else 'Not assigned'}")
        print("-" * 40)


    
def get_user_group(session, user_id, site_id, visit_date):
    """
    Retrieves and prints the group info for a given user on a specific visit.
    """
    dateOfVisit = visit_date.date()

    booking = (
        session.query(Booking)
        .filter(
            Booking.user_id == user_id,
            Booking.tourist_site_id == site_id,
            Booking.group.has(Group.visiting_date.cast(Date) == dateOfVisit),
            Booking.confirmed == True
        )
        .first()
    )

    if not booking:
        print("No confirmed booking found for this user on the given date.")
        return

    group = booking.group

    group_bookings = [b for b in group.bookings if b.tourist_site_id == site_id]
    group_size = sum(b.group_size for b in group_bookings)

    print(f"\nCurrent Group for User ID: {user_id}")
    print(f"Group ID: {group.id}")
    print(f"Total Group Members: {group_size}")
    print(f"Tour Guide: {group.tour_guide.fullname if group.tour_guide else 'Not assigned'}")
    print(f"Cab Driver: {group.cab.driver_name if group.cab else 'Not assigned'}")
    print("-" * 40)


