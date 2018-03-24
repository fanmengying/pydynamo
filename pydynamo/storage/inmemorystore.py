from .iterator import Iterator
from .binarysearchtree import BinarySearchTree
from .store import Store


class InMemoryStore(Store):
    def __init__(self, store_name):
        self.store_name = store_name
        self.database = BinarySearchTree()

    def set(self, key: str, value: str) -> None:
        if self.database.contain(key):
            self.database.update(key, value)
        else:
            self.database.insert(key, value)

    def get(self, key: str) -> str:
        if not self.database.contain(key):
            return None
        else:
            return self.database.get(key)

    def iterator(self) -> Iterator:
        return Iterator(self.database)

    def remove(self, key:str) -> None:
        self.database.remove_node(key)