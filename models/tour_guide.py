from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from  db import Base

class TourGuide(Base):
    """
    This is a class that creates a tour guide model in the database, it inherits from Base.
    It has attributes like fullname, email, country, created_at, updated_at, bookings, and groups.
    It also has a class method called create_tour_guide to create a tour guide instance.
    """
    __tablename__ = "tour_guides"
from datetime import datetime
import uuid
from  db import Base

class TourGuide(Base):
    _tablename_ = "tour_guides"

    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    
    bookings = relationship("Booking", back_populates="tour_guide")
    groups = relationship("Group", back_populates="tour_guide")


    @classmethod
    def create_tour_guide(cls, fullname, email, country):
        tour_guide = cls(
            fullname=fullname,
            email=email,
            country=country
        )
        return tour_guide
    

    def __repr__(self):
        return f"TourGuideId='{self.id}'\nFullname='{self.fullname}'\nEmail='{self.email}'\nCountry='{self.country}'"
    

