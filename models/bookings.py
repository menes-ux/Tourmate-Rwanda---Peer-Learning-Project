from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from  db import Base


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_size = Column(String, nullable=False)
    visting_date = Column(DateTime, nullable=False)
    price = Column(String, nullable=False)
    confirmed = Column(Boolean, default=False)

    tour_guide_id = Column(UUID(as_uuid=True), ForeignKey('tour_guides.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    cab_id = Column(UUID(as_uuid=True), ForeignKey('cabs.id'), nullable=False)
    
    user = relationship("User", back_populates="bookings")
    cab = relationship("Cab", back_populates="bookings")
    tour_guide = relationship("TourGuide", back_populates="bookings")
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


    @classmethod
    def create(cls, group_size, visting_date, price, tour_guide_id, user_id, cab_id):
        booking = cls(
            group_size=group_size,
            visting_date=visting_date,
            price=price,
            tour_guide_id=tour_guide_id,
            user_id=user_id,
            cab_id=cab_id
        )
        return booking
    
    def __repr__(self):
        return (f"BookingId='{self.id}'\n"
                f"group_size='{self.group_size}'\n"
                f"visting_date='{self.visting_date}'\n"
                f"price='{self.price}'\n"
                f"confirmed='{self.confirmed}'\n"
                f"tour_guide_id='{self.tour_guide_id}'\n"
                f"user_id='{self.user_id}'\n"
                f"cab_id='{self.cab_id}'")