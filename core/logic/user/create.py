from typing import Tuple
from PIL import Image
from .base import BaseUser
from sqlalchemy.orm import Session
from models.models import User
from models.config import engine
from sqlalchemy.types import NULLTYPE



class CreateUser(BaseUser):
    """
    Класс для создания нового пользователя.
    """

    def __init__(self, id_number: int, username: str, password: str,
                role_id: int, gender: str,
                firstname: str = NULLTYPE, lastname: str = NULLTYPE,
                photo: Image = NULLTYPE, email: str = NULLTYPE,
                phone: str = NULLTYPE, direction_id: int = NULLTYPE,
                event_id: int = NULLTYPE) -> Tuple[str, int]:
        self.id_number = id_number
        self.username = username
        self.password = password
        self.role_id = role_id
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.photo = photo
        self.email = email
        self.phone = phone
        self.direction_id = direction_id
        self.event_id = event_id


    def create(self):
        """
        Метод для создания нового пользователя в базе данных.
        Возвращает:
            str: Сообщение об успешности или ошибке
            int: Код ответа
        """

        try:
            # Создаем сессию
            with Session(engine) as session:
                # Создаем нового пользователя и сохраняем его в базу данных
                user = User(
                    id_number=self.id_number,
                    username=self.username,
                    password=self.password,
                    role_id=self.role_id,
                    gender=self.gender,
                    firstname=self.firstname,
                    lastname=self.lastname,
                    photo=self.photo,
                    email=self.email,
                    phone=self.phone,
                    direction_id=self.direction_id,
                    event_id=self.event_id
                )
                session.add(user)
                session.commit()

            return "Пользователь успешно создан", 200
        except Exception as e:
            return f"Ошибка при создании пользователя: {str(e)}", 400
        



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""