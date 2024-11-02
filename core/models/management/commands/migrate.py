from django.core.management.base import BaseCommand
from models.models import Base
from models.config import engine


"""

#SECTION - ============ Файл для создания кастомных комманд в Django ============

Используется для создания таблиц в базе данных.

Дабы активировать данный файл с классом для создания таблиц в базе данных,
нам нужно прописать следующую комманду в консоли:
```bash
python manage.py migrate
```

"""


class Command(BaseCommand):
    help = 'Эта команда создает таблицы в базе данных'

    def handle(self, *args, **options):
        """
        Данная функция активируется, когда в консоли прописывается
        следующая комманда:
        ```
        python manage.py migrate
        ```
        """
        # Создаем таблицы в базе данных
        Base.metadata.create_all(engine)