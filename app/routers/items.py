from fastapi import APIRouter, HTTPException, status

from app.schemas import Item, ItemCreate, ItemUpdate
from app.store import store

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[Item])
def list_items() -> list[Item]:
    return store.list()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemCreate) -> Item:
    return store.create(data)


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemUpdate) -> Item:
    item = store.update(item_id, data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if not store.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
