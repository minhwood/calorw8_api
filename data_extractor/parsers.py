import csv

from sqlalchemy.orm.session import Session

from .configurations import *
from .models import FoodDto, CategoryDto, FoodNutrientDto, NutrientDto
from db.base import SessionLocal

class Parser():

    DTO_OBJECT = None
    SOURCE_FILE:str = ""

    def extract(self):
        with open(f"{DATA_SOURCE}/{self.SOURCE_FILE}", encoding="latin1") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list([row for row in csv_reader])
            return data

    def transform(self, extracted_data):
        return [
            self.DTO_OBJECT(**row).transform() for row in extracted_data 
            if self.DTO_OBJECT(**row).transform() is not None
        ]
        

    def load(self, transformed_data):
        session:Session = SessionLocal()
        session.bulk_save_objects(transformed_data)
        session.commit()
        session.close()


    def execute(self):
        extracted_data = self.extract()
        transformed_data = self.transform(extracted_data)
        self.load(transformed_data)

class FoodParser(Parser):

    DTO_OBJECT = FoodDto
    SOURCE_FILE = FOOD_FILE

class CategoryParser(Parser):

    DTO_OBJECT = CategoryDto
    SOURCE_FILE = FOOD_CATEGORY_FILE

class NutrientParser(Parser):

    DTO_OBJECT = NutrientDto
    SOURCE_FILE = NUTRIENTS_FILE

class FoodNutrientParser(Parser):

    DTO_OBJECT = FoodNutrientDto
    SOURCE_FILE = FOOD_NUTRIENTS_FILE