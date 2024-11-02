from django.core.management.base import BaseCommand
from models.models import Role
from models.config import engine
from sqlalchemy.orm import Session



"""

# SECTION - ============ Файл для создания кастомных комманд в Django ============

Данный файл используется для создания базовых ролей в базе данных.

Дабы активировать данный файл с классом для создания базовых ролей в базе данных,
нам нужно прописать следующую комманду в консоли:
```bash
python manage.py create_roles
```

"""


class Command(BaseCommand):
    help =  """
            Данная команда создает базовые роли:
                - пользователь
                - организатор
                - жюри
                - модератор
            """
    
    def handle(self, *args, **options):
        """
        Данная функция активируется, когда в консоли прописывается
        следующая комманда:
        ```
        python manage.py create_roles
        ```
        """
        try:
            # Создаем сессию
            with Session(engine) as session:

                # Создаем роли
                roles = [
                    Role(name="пользователь"),
                    Role(name="организатор"),
                    Role(name="жюри"),
                    Role(name="модератор"),
                ]

                # Сохраняем роли в базу данных
                session.add_all(roles)
                session.commit()

                self.stdout.write(self.style.SUCCESS("Базовые роли успешно созданы!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при создании базовых ролей: {e}"))