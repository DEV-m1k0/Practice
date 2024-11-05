import random
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.config import engine
from models.models import User


"""

#SECTION - ================= Пакет для генерации различных данных =================

"""


def unique_id_number() -> int:
    """
    Функция для генерирации уникального идентификатора из чисел от 0 до 1000000
    """

    id_number: int = random.randint(0, 1000000)
    try:
        # Проверяем, есть ли уже такой идентификатор в базе
        while True:
            # Генерируем случайный идентификатор
            id_number = random.randint(0, 1000000)
            
            # Создаем sql запрос
            users_sql_row = select(User)

            # Используем сессию для выполнения запроса и получения данных
            with Session(engine) as session:
                # Получаем всех пользователей
                users = session.scalars(users_sql_row).all()

            check_id_number: bool = False

            # Проверяем, есть ли такой идентификатор у другого пользователя
            for i in range(len(users)):
                if users[i].id_number == id_number:
                    check_id_number = True
                    break

            if not check_id_number:
                return id_number
    except:
        return id_number
    


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""