from logic.base import Entity


"""

#SECTION - ============== Определение базовых классов для мероприятий ==============

"""


class BaseEvent(Entity):
    """
    Класс для определения общего поведения мероприятий.
    """

    def get(self):
        return super().get()
    
    def save(self):
        return super().save()
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()