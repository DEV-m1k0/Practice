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

session = Session(engine)