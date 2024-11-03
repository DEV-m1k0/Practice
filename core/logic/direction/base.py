from abc import ABC, abstractmethod


"""

#SECTION - ============= Определение базовых классов для направлений =============

"""



class BaseDirection(ABC):
    """
    Абстрактный класс для определения общего поведения направлений.
    """
    @abstractmethod
    def create():
        pass
    
    @abstractmethod
    def get_name_by_id():
        pass

    @abstractmethod
    def get_id_by_name():
        pass