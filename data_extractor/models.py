from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from db.models import Category, Food, FoodNutrient, Nutrient

class Dto(BaseModel):

    def transform(self):
        pass

class FoodDto(Dto):
    """
    Core food object
    """

    id: int = Field(..., alias="FoodID")
    code: int = Field(..., alias="FoodCode")
    category_id: int = Field(..., alias="FoodGroupID")
    description: str = Field(..., alias="FoodDescription")
    date_of_entry: str = Field(..., alias="FoodDateOfEntry")
    date_of_pub: str = Field(..., alias="FoodDateOfPublication")
    country_code: str = Field(..., alias="CountryCode")
    scientific_name: str = Field(..., alias="ScientificName")

    def transform(self) -> Food:
        return Food(
            id= self.id,
            code=self.code,
            category_id=self.category_id,
            description=self.description,
            date_of_entry=self.date_of_entry,
            date_of_pub=self.date_of_pub,
            country_code=self.country_code,
            scientific_name=self.scientific_name           
        )


class CategoryDto(Dto):
    """
    Food Category
    """

    id:int = Field(..., alias="FoodGroupID")
    code: int = Field(..., alias="FoodGroupCode")
    name: str = Field(..., alias="FoodGroupName")

    def transform(self) -> Category:
        return Category(
            id=self.id,
            code=self.code,
            name=self.name
        )


class NutrientDto(Dto):
    """
    Detail of each nutrient information
    """
    id: int = Field(..., alias="NutrientID")
    code: int = Field(..., alias="NutrientCode")
    symbol: str = Field(..., alias="NutrientSymbol")
    unit: str = Field(..., alias="NutrientUnit")
    name: str = Field(..., alias="NutrientName")
    tagname: str = Field(..., alias="Tagname")
    decimals: int = Field(..., alias="NutrientDecimals")

    def transform(self) -> Nutrient:
        return Nutrient(
            id=self.id,
            code=self.code,
            symbol=self.symbol,
            unit=self.unit,
            name=self.name,
            tagname=self.tagname,
            decimal=self.decimals
        )

class FoodNutrientDto(Dto):
    """
    Food nutrients base on 100g editable portion
    """

    food_id: int = Field(..., alias="FoodID")
    nutrient_id: int = Field(..., alias="NutrientID")
    nutrient_value: float = Field(..., alias="NutrientValue")
    standard_error: str = Field(..., alias="StandardError")
    numberof_observations: str = Field(..., alias="NumberofObservations")
    nutrient_source_id: int = Field(..., alias="NutrientSourceID")
    nutrient_date_of_entry: str = Field(..., alias="NutrientDateOfEntry")


    def transform(self) -> FoodNutrient:

        if self.nutrient_id in [328,]:
            return None
        return FoodNutrient(
            food_id=self.food_id,
            nutrient_id=self.nutrient_id,
            nutrient_value=self.nutrient_value
        )