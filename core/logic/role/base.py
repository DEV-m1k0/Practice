from logic.base import Entity


"""

#SECTION - ================= Определение базовых классов для ролей =================

"""


class BaseRole(Entity):
    """
    Класс для определения общего поведения ролей.
    """

    def get(self):
        return super().get()
    
    def save(self):
        return super().save()
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()
    

"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""