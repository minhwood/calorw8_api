from typing import Any
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class ModelBase:
    id: Any
    __name__: str
    
    @declared_attr
    def __tablename__(cls):
        """
        Auto generate database name
        from Class name
        """
        return cls.__name__.lower()


class Category(ModelBase):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    name = Column(String(100))


class Food(ModelBase):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    category_id = Column(ForeignKey("category.id"))
    description = Column(String(255))
    date_of_entry = Column(String(255))
    date_of_pub = Column(String(255))
    country_code = Column(String(10))
    scientific_name = Column(String(100))


class Nutrient(ModelBase):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    symbol = Column(String(100))
    unit = Column(String(100))
    name = Column(String(100))
    tagname = Column(String(100))
    decimal = Column(Float)


class FoodNutrient(ModelBase):
    id = Column(Integer, primary_key=True)
    food_id = Column(ForeignKey("food.id"))
    nutrient_id = Column(ForeignKey("nutrient.id"))
    nutrient_value = Column(Float)


