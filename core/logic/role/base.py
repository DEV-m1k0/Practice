from abc import ABC, abstractmethod


"""

#SECTION - ================= Определение базовых классов для ролей =================

"""


class BaseRole(ABC):
    """
    Абстрактный класс для определения общего поведения ролей.
    """

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_role_by_id(self):
        pass

    @abstractmethod
    def get_id_by_role(self):
        pass