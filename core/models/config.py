from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session

"""

#SECTION - ================ Конфигурационный файл для SqlAlchemy ================

В данном файле осуществлеятся конфигурация SqlAlchemy.

engine - в SQLAlchemy используется для создания и управления подключением к
базе данных. Она играет ключевую роль в процессе взаимодействия с
базой данных через ORM (Object-Relational Mapping)

"""


# Формируем словарь с нужными значениями для подключения к базе данных
url_db = {
    "drivername": "sqlite",
    "database": "practice.db"
}

# Формируем engine для работы с базой данных
engine = create_engine(
            url=URL.create(**url_db),
            echo=True
        )

# Создаем сессию
session = Session(engine)



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""