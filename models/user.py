from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    country = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    bookings = relationship("Booking", back_populates="user")
    
    
    @classmethod
    def create_user(cls, fullname, email, password, country):
        user = cls(
            fullname=fullname,
            email=email,
            password=password,
            country=country
        )
        return user

    def __repr__(self):
        return f"userId='{self.id}'\nfullname='{self.fullname}'\nemail='{self.email}'\ncountry='{self.country}'"

