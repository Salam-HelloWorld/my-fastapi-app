from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0)
    in_stock: bool = True


class ItemCreate(ItemBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Book", "description": "A paperback novel", "price": 12.5, "in_stock": True}
            ]
        }
    }


class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    in_stock: bool | None = None

    model_config = {"json_schema_extra": {"examples": [{"price": 9.99, "in_stock": False}]}}


class Item(ItemBase):
    id: int
