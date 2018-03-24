import unittest
from storage.store import Store
from storage.engine import InMemoryStorageEngine


class InMemoryStorageEngineTest(unittest.TestCase):
    def test_smoke(self) -> None:
        engine = InMemoryStorageEngine()
        self.assertTrue(isinstance(engine, InMemoryStorageEngine))

    def test_creat_store(self):
        new_store = InMemoryStorageEngine().create_store("test")
        self.assertTrue(isinstance(new_store, Store))

    def test_get_store(self):
        #new_store = StorageEngine().create_store("test")
        #self.assertEqual(StorageEngine().get_store("test"), new_store)
        pass




