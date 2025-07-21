from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

from db import Base


class Site(Base):
    __tablename__ = 'tourist_sites'

    site_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sitename = Column(String, nullable=False)
    location = Column(String, unique=True, nullable=False)
    gatepass = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    

    @classmethod
    def create_touristsite(cls, sitename, location, gatepass):
        user = cls(
            sitename=sitename,
            location=location,
            gatepass=gatepass
        )
        return user

    def __repr__(self):
        return f"Site_id='{self.site_id}'\nsitename='{self.sitename}'\nlocation='{self.location}'\ngatepass='{self.gatepass}'"

    
