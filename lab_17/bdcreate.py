from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy import Warehouse, Supplier, Product, Stock, create_db

def fill_data():
    engine = create_engine('sqlite:///warehouse.db', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    supplier1 = Supplier(name="Поставщик А", contact_info="contactA@example.com")
    supplier2 = Supplier(name="Поставщик Б", contact_info="contactB@example.com")

    product1 = Product(name="Товар 1", supplier=supplier1)
    product2 = Product(name="Товар 2", supplier=supplier1)
    product3 = Product(name="Товар 3", supplier=supplier2)
    product4 = Product(name="Товар 4", supplier=supplier2)

    warehouse1 = Warehouse(name="Склад Москва", location="Москва")
    warehouse2 = Warehouse(name="Склад СПб", location="Санкт-Петербург")

    stock1 = Stock(warehouse=warehouse1, product=product1, quantity=100)
    stock2 = Stock(warehouse=warehouse1, product=product3, quantity=50)
    stock3 = Stock(warehouse=warehouse2, product=product2, quantity=200)
    stock4 = Stock(warehouse=warehouse2, product=product4, quantity=150)

    session.add_all([supplier1, supplier2, product1, product2, product3, product4,
                     warehouse1, warehouse2, stock1, stock2, stock3, stock4])
    session.commit()
    session.close()

create_db()
fill_data()
