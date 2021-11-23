from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def search_foods(search_txt: str = None, category: str = None, page: int = 1):
    return {
        "search_txt": search_txt,
        "category": category,
        "page": page,
    }


@router.get("/{id}/")
def food_detail(id: int):
    print("Food id", id)
    return {
        "id": id
    }