from django.core.management.base import BaseCommand
from models.models import User, Role
from models.config import engine
from django.contrib.auth.hashers import make_password
from sqlalchemy import select
from sqlalchemy.orm import Session
import random


"""

# SECTION - ============ Файл для создания кастомных комманд в Django ============

Данный файл используется для создания базовых пользователей в базе данных.

Дабы активировать данный файл с классом для базовых пользователей в базе данных,
нам нужно прописать следующую комманду в консоли:
```bash
python manage.py create_base_users
```

"""



class Command(BaseCommand):
    help = 'Данная комманда создает базовых пользователей'

    def handle(self, *args, **options):
        """
        Данная функция активируется, когда в консоли прописывается
        следующая комманда:
        ```
        python manage.py create_base_users
        ```
        """

        try:
            # Создаем сессию
            with Session(engine) as session:

                # NOTE - Создаем пользователя с ролью 'пользователь'
                # Создаем уникальный идентификатор для пользователя
                user_id_number: int
                while True:
                    with Session(engine) as session:
                        # Генерируем случайный идентификатор
                        user_id_number = random.randrange(0, 1000000, 1)
                        
                        # Создаем sql запрос
                        users_sql_row = select(User)

                        # Получаем всех пользователей
                        users = session.scalars(users_sql_row).all()

                        check_id_number: bool = False

                        # Проверяем, есть ли такой идентификатор у другого пользователя
                        for i in range(len(users)):
                            if users[i].id_number == user_id_number:
                                check_id_number = True
                                break

                        if not check_id_number:
                            break


                # Формируем пароль для пользователя
                user_password = make_password("user")
                
                # Находим роль по имени 'пользователь'
                user_role = select(Role).where(Role.name == "пользователь")

                # Получаем id данной роли
                user_role_id = session.scalar(user_role).id

                # Создаем нового пользователя с ролью 'пользователь' и паролем 'user'
                new_user = User(id_number=user_id_number,
                                username="user", password=user_password,
                                role_id=user_role_id, gender="мужчина")
                

                # NOTE - Создаем пользователя с ролью 'организатор'
                # Создаем уникальный идентификатор для пользователя
                organizer_id_number: int
                while True:
                    with Session(engine) as session:
                        # Генерируем случайный идентификатор
                        organizer_id_number = random.randrange(0, 1000000, 1)
                        
                        # Создаем sql запрос
                        users_sql_row = select(User)

                        # Получаем всех пользователей
                        users = session.scalars(users_sql_row).all()

                        check_id_number: bool = False

                        # Проверяем, есть ли такой идентификатор у другого пользователя
                        for i in range(len(users)):
                            if users[i].id_number == organizer_id_number:
                                check_id_number = True
                                break

                        if not check_id_number:
                            break

                # Формируем пароль для организатора
                organizer_password = make_password("organizer")
                
                # Находим роль по имени 'организатор'
                organizer_role = select(Role).where(Role.name == "организатор")

                # Получаем id данной роли
                organizer_role_id = session.scalar(organizer_role).id

                # Создаем нового пользователя с ролью 'организатор' и паролем 'organizer'
                new_organizer = User(id_number=organizer_id_number,
                                     username="organizer", password=organizer_password,
                                     role_id=organizer_role_id, gender="мужчина")
                
                
                # NOTE - Создаем пользователя с ролью 'модератор'
                # Создаем уникальный идентификатор для пользователя
                moderator_id_number: int
                while True:
                    with Session(engine) as session:
                        # Генерируем случайный идентификатор
                        moderator_id_number = random.randrange(0, 1000000, 1)
                        
                        # Создаем sql запрос
                        users_sql_row = select(User)

                        # Получаем всех пользователей
                        users = session.scalars(users_sql_row).all()

                        check_id_number: bool = False

                        # Проверяем, есть ли такой идентификатор у другого пользователя
                        for i in range(len(users)):
                            if users[i].id_number == moderator_id_number:
                                check_id_number = True
                                break

                        if not check_id_number:
                            break

                # Формируем пароль для модератора
                moderator_password = make_password("moderator")
                
                # Находим роль по имени 'модератор'
                moderator_role = select(Role).where(Role.name == "модератор")

                # Получаем id данной роли
                moderator_role_id = session.scalar(moderator_role).id

                # Создаем нового пользователя с ролью 'модератор' и паролем 'moderator'
                new_moderator = User(id_number=moderator_id_number,
                                     username="moderator", password=moderator_password,
                                     role_id=moderator_role_id, gender="мужчина")


                # NOTE - Создаем пользователя с ролью 'жюри'
                # Создаем уникальный идентификатор для пользователя
                jury_id_number: int
                while True:
                    with Session(engine) as session:
                        # Генерируем случайный идентификатор
                        jury_id_number = random.randrange(0, 1000000, 1)
                        
                        # Создаем sql запрос
                        users_sql_row = select(User)

                        # Получаем всех пользователей
                        users = session.scalars(users_sql_row).all()

                        check_id_number: bool = False

                        # Проверяем, есть ли такой идентификатор у другого пользователя
                        for i in range(len(users)):
                            if users[i].id_number == jury_id_number:
                                check_id_number = True
                                break

                        if not check_id_number:
                            break
                        
                # Формируем пароль для пользователя
                jury_password = make_password("jury")
                
                # Находим роль по имени 'jury'
                jury_role = select(Role).where(Role.name == "жюри")

                # Получаем id данной роли
                jury_role_id = session.scalar(jury_role).id

                # Создаем нового пользователя с ролью 'жюри' и паролем 'jury'
                new_jury = User(id_number=jury_id_number,
                                username="jury", password=jury_password,
                                role_id=jury_role_id, gender="мужчина")
                                

                # Сохраняем пользователей в базу данных
                session.add_all([new_user, new_organizer, new_jury, new_moderator])
                session.commit()

                self.stdout.write(self.style.SUCCESS("Базовые пользователи созданы успешно"))
                
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при создании базовых пользователей: {e}"))