from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from  db import Base

class Cab(Base):
    __tablename__ = 'cabs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cab_number = Column(String, nullable=False, unique=True)
    driver_name = Column(String, nullable=False)
    driver_contact = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @classmethod
    def create_cab(cls, cab_number, driver_name, driver_contact):
        cab = cls(
            cab_number=cab_number,
            driver_name=driver_name,
            driver_contact=driver_contact
        )
        return cab

    def __repr__(self):
        return f"CabId='{self.id}'\ncab_number='{self.cab_number}'\ndriver_name='{self.driver_name}'\ndriver_contact='{self.driver_contact}'"
    
    