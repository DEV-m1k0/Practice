from logic.base import Entity


"""

#SECTION - ============= Определение базовых классов для направлений =============

"""



class BaseDirection(Entity):
    """
    Класс для работы с направлениями
    """

    def save(self):
        return super().save()
    
    def delete(self):
        return super().delete()
    
    def update(self):
        return super().update()
    
    def get(self):
        return super().get()
    

"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""