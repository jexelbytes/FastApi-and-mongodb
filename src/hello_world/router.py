from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from hello_world.schemas import ProductReview, UpdateProductReview


router = APIRouter()

@router.get('/product')
async def get_products():
    data = await ProductReview.find_all().to_list()
    return data

@router.post('/product')
async def add_product(review: ProductReview):
    product = await review.create()
    return product

@router.put("/{id}", response_description="Review record updated")
async def update_student_data(id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await review.update(update_query)
    return review

