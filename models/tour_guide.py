from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from  db import Base

class TourGuide(Base):
    __tablename__ = "tour_guides"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
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
    