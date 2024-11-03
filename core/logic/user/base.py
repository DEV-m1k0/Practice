from abc import ABC, abstractmethod


"""

#SECTION - ============= Определение базовых классов для пользователей =============

"""


class BaseUser(ABC):
    """
    Абстрактный класс для определения общего поведения пользователей.
    """
    @abstractmethod
    def create():
        pass