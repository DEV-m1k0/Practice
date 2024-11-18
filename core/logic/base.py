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
    


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""