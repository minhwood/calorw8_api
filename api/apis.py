from fastapi import APIRouter

from .controllers import foods

api_router = APIRouter()

# health check
api_router.include_router(foods.router, prefix="/foods", tags=["foods"])
