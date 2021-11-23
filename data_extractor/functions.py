from .parsers import CategoryParser, FoodNutrientParser, FoodParser, NutrientParser

def migrate():
    print("Start migrating data ...")
    CategoryParser().execute()
    FoodParser().execute()
    NutrientParser().execute()
    FoodNutrientParser().execute()
    print("Finish food data migration")