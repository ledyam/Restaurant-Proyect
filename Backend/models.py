from sqlalchemy import Column, Integer, String, Time,Date
from database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Integer)
    categoria = Column(String)
    
    
class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    identification = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    people = Column(Integer, nullable=False)
    message = Column(String, nullable=True)


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    identification = Column(String, nullable=False)
    username = Column (String , nullable=False )
    phone = Column(String, nullable=False)
    email = Column(String , nullable=False )
    ocupation = Column(String, nullable=False)
    password = Column(String, nullable=False)