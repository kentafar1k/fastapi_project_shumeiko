from sqlalchemy import Column, Integer, String, JSON

from database import Base

class Hotels(Base):
    __tablename__ = 'hotels'  # название таблицы

    id = Column(Integer, primary_key=True)  # primary-первичный(генерится сам начиная с 1)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON, nullable=False)
    room_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
