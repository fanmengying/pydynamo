from typing import Any
from .store import Store
from abc import ABCMeta
from abc import ABC
from abc import abstractmethod


class StorageEngine(ABC):
    @abstractmethod
    def create_store(self, store_name: str) -> Store:
        pass

    @abstractmethod
    def get_store(self, store_name: str) -> Store:
        pass


class InMemoryStorageEngine(StorageEngine):
    def __init__(self):
        self.stores = {}

    def create_store(self, store_name: str) -> Store:
        self.stores[store_name] = Store(store_name)
        return self.stores[store_name]

    def get_store(self, store_name: str) -> Store:
        if store_name in self.stores:
            return self.stores[store_name]
        else:
            return None


