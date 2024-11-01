from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker


#SECTION - ================ Конфигурационный файл для SqlAlchemy ================


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