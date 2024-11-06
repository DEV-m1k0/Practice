from django.core.management.base import BaseCommand
from models.models import Base
from models.config import session


"""

#SECTION - ============ Файл для создания кастомных комманд в Django ============

Данный файл используется для создания таблиц в базе данных.

Дабы активировать данный файл с классом для создания таблиц в базе данных,
нам нужно прописать следующую комманду в консоли:
```bash
python manage.py create_tables
```

"""


class Command(BaseCommand):
    help = 'Эта команда создает таблицы в базе данных'

    def handle(self, *args, **options):
        """
        Данная функция активируется, когда в консоли прописывается
        следующая комманда:
        ```
        python manage.py create_tables
        ```
        """

        try:
            # Создаем таблицы в базе данных
            Base.metadata.create_all(session.get_bind())
            self.stdout.write(self.style.SUCCESS('Таблицы успешно созданы!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при создании таблиц: {e}'))