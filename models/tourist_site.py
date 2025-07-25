from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import random
import string

from db import Base


def generateRandomSiteCode():
    randomValue = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"SITE-{randomValue}"


class TouristSite(Base):
    """
    This is a class that represents a tourist site in the database.
    It inherits from the Base class which is a declarative base for SQLAlchemy models.
    """
    __tablename__ = 'tourist_sites'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    site_code = Column(String, unique=True, default=generateRandomSiteCode)  
    sitename = Column(String, nullable=False)
    location = Column(String, unique=True, nullable=False)
    gatepassfee = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    bookings = relationship("Booking", back_populates="tourist_sites")

    @classmethod
    def create_touristsite(cls, sitename, location, gatepassfee):
        """
            This is a class method to create a new TouristSite instance.
        """
        touristsite = cls(
            sitename=sitename,
            location=location,
            gatepassfee=gatepassfee
        )
        return touristsite

    def __repr__(self):
        return (
            f"| Attribute       | Value                 |\n"
            f"+-----------------+------------------------+\n"
            f"| Site Code       | {self.site_code:<24} |\n"
            f"| Sitename        | {self.sitename:<24} |\n"
            f"| Location        | {self.location:<24} |\n"
            f"| Gatepass Fee    | {self.gatepassfee:<24} |\n"
        )
