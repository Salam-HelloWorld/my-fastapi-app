"""Simple in-memory storage. Data is lost when the server restarts."""
from threading import Lock

from app.schemas import Item, ItemCreate, ItemUpdate


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id = 1
        self._lock = Lock()

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def create(self, data: ItemCreate) -> Item:
        with self._lock:
            item = Item(id=self._next_id, **data.model_dump())
            self._items[item.id] = item
            self._next_id += 1
            return item

    def update(self, item_id: int, data: ItemUpdate) -> Item | None:
        with self._lock:
            existing = self._items.get(item_id)
            if existing is None:
                return None
            updated = existing.model_copy(update=data.model_dump(exclude_unset=True))
            self._items[item_id] = updated
            return updated

    def delete(self, item_id: int) -> bool:
        with self._lock:
            return self._items.pop(item_id, None) is not None

    def clear(self) -> None:
        with self._lock:
            self._items.clear()
            self._next_id = 1


store = ItemStore()
