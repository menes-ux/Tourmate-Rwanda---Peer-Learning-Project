from db import Base
from sqlalchemy import Column,  DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Group(Base):
    _tablename_ = 'groups'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    visiting_date = Column(DateTime, nullable=False)
    tour_guide_id = Column(UUID(as_uuid=True), ForeignKey('tour_guides.id'), nullable=False)
    cab_id = Column(UUID(as_uuid=True), ForeignKey('cabs.id'), nullable=False)

    bookings = relationship("Booking", back_populates="group")
    cab = relationship("Cab", back_populates="groups")
    tour_guide = relationship("TourGuide", back_populates="groups")