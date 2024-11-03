from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Абстрактный класс для всех сущностей.
    """
    @abstractmethod
    def save(self): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def get(self): pass

    def __throw_exception(self, exception):
        raise Exception(exception)