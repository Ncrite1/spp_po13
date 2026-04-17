from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TransportType(Base):
    __tablename__ = "transport_types"

    type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class Route(Base):
    __tablename__ = "routes"

    route_id = Column(Integer, primary_key=True, index=True)
    route_number = Column(String, nullable=False)
    type_id = Column(Integer, ForeignKey("transport_types.type_id"))

    transport_type = relationship("TransportType")