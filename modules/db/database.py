from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def add(table, key, value):
        pass

    @abstractmethod
    def update(table, key, value):
        pass

    @abstractmethod
    def delete(table, key):
        pass

    @abstractmethod
    def get(table, key):
        pass