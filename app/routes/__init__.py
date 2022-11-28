from fastapi import APIRouter

from .types import router as types_router
from .posts import router as posts_router

router = APIRouter()
router.include_router(types_router, prefix='/types', tags=['types'])
router.include_router(posts_router, prefix='/posts', tags=['posts'])
