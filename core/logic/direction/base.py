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