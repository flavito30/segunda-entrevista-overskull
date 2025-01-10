from sqlalchemy import Column, Integer, String , DECIMAL , Double
from app.database import Base


class Product (Base) : 
    __tablename__ = "productos"
    id  = Column ( Integer , primary_key = True , index = True )
    nombre = Column ( String , index = True , unique=True )
    categoria = Column ( String , index = True )
    precio = Column ( Double , index = True )  
    stock = Column ( Integer , index = True )

    
