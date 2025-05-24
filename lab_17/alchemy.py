from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Warehouse(Base):
    __tablename__ = 'warehouses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    stocks = relationship("Stock", back_populates="warehouse")

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

    supplier = relationship("Supplier", back_populates="products")
    stocks = relationship("Stock", back_populates="product")

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, ForeignKey('warehouses.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=0)

    warehouse = relationship("Warehouse", back_populates="stocks")
    product = relationship("Product", back_populates="stocks")

def create_db():
    engine = create_engine('sqlite:///warehouse.db', echo=False)
    Base.metadata.create_all(engine)
