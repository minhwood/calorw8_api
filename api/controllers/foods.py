from re import search
from fastapi import APIRouter, Depends
from sqlalchemy.orm import eagerload
from sqlalchemy.orm.session import Session

from db.models import Food, Category
from api.dependencies import repository

router = APIRouter()

@router.get("/categories")
def get_all_categories(db: Session = Depends(repository)):
    categories = db.query(Category).all()
    return categories

@router.get("/")
def search_foods(
    db: Session = Depends(repository),
    search_txt: str = "", 
    category: int = None, 
    page: int = 1
    ) -> Food:
    if page < 1: page = 1
    limit = 10
    offset = limit*(page - 1)
    conditions = []
    
    conditions.append(Food.description.like(f"%{search_txt}%"))
    # Only add this condition if received categories filter
    if category:
        conditions.append(Food.category_id==category)

    foods = db.query(Food)\
        .filter(*conditions)\
        .offset(offset)\
        .limit(limit)\
        .all()
    return foods


@router.get("/{id}/")
def food_detail(
    *,
    db: Session = Depends(repository), 
    id: int
    ) -> Food:
    food = db.query(Food).options(eagerload("*")).get(id)
    return food