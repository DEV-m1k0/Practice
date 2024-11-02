from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

"""

#SECTION - ================ Конфигурационный файл для SqlAlchemy ================

В данном файле осуществлеятся конфигурация SqlAlchemy.

Помимо конфигурации SqlAlchemy, мы инициализируем переменные, при помщи которых
мы в дальнешем будем взаимодействовать с нашей базой данных, а именно:
1. engine
2. Session

engine - в SQLAlchemy используется для создания и управления подключением к
базе данных. Она играет ключевую роль в процессе взаимодействия с
базой данных через ORM (Object-Relational Mapping)

Session - представляет собой фабрику сессий, которая служит для создания
объектов-сессий, используемых для выполнения операций с данными базы данных
через ORM (Object-Relational Mapping).

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

# Создаем сессию при помощи которой мы будем создавать/редактировать/удалять данные
Session = sessionmaker(engine, autoflush=False, autocommit=False)