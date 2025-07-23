from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import Base


class TouristSite(Base):
    __tablename__ = 'tourist_sites'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sitename = Column(String, nullable=False)
    location = Column(String, unique=True, nullable=False)
    gatepassfee = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    
    @classmethod
    def create_touristsite(cls, sitename, location, gatepassfee):
        user = cls(
            sitename=sitename,
            location=location,
            gatepassfee=gatepassfee
        )
        return user

    def __repr__(self):
        return (
            f"| Attribute       | Value            |\n"
            f"+-----------------+----------------------+\n"
            f"| Sitename        | {self.sitename:<20} |\n"
            f"| Location        | {self.location:<20} |\n"
            f"| Gatepass Fee    | {self.gatepassfee:<20} |\n"
        )

