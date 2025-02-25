import re


"""

#SECTION - ===================== Пакет для валидации данных =====================

"""


def phone_is_valid(phone: str):
    """
    Валидация номера телефона
    """

    try:
        # Проверка количества '-' в номере
        if phone.count('-') != 3:
            return False, 'Номер телефона должен быть в следующем формате: +7(999)-999-99-99'

        

        # Проверка наличия "+" в начале номера телефона
        if phone[0] != '+':
            return False, 'Номер телефона должен быть в следующем формате: +7(999)-999-99-99'

        # Проверка наличия скобок в номере телефона
        if not '(' == phone[2] and not ')' in phone[6]:
            return False, 'Номер телефона должен быть в следующем формате: +7(999)-999-99-99'

        # Проверка длины номера телефона
        if len(phone) != 17:
            return False, 'Номер телефона должен быть в следующем формате: +7(999)-999-99-99'

        # Проверка наличия дефиса в номере телефона
        if not '-' in phone:
            return False, 'Номер телефона должен быть в следующем формате: +7(999)-999-99-99'

        return True, 'Номер телефона валиден.'
    except Exception as e:
        return False, str(e)


def email_is_valid(email: str):
    """
    Валидация почты
    """

    try:
        # Проверка наличия "@" в адресе
        if '@' not in email:
            return False, 'Адрес электронной почты должен содержать "@".'

        # Проверка наличия двух "@"
        if email.count('@')!= 1:
            return False, 'Адрес электронной почты должен содержать только одну "@".'

        # Проверка наличия доменного имени
        domain_name = email.split('@')[1]
        if '.' not in domain_name:
            return False, 'Доменное имя должно содержать хотя бы один "." после "@".'

        # Проверка наличия доменного имени начинающегося с цифры
        if domain_name[0].isdigit():
            return False, 'Доменное имя не может начинаться с цифры.'
        
        # Проверка наличия одной точки в доменном имени
        if not domain_name.count('.') == 1:
            return False, 'Доменное имя должно содержать одну "." после "@".'

        return True, 'Адрес электронной почты валиден.'
    except Exception as e:
        return False, str(e)


def fullname_is_valid(full_name: str):
    """
    Валидация полного имени
    """

    try:
        # Проверка наличия нужного количества слова в полном имени
        if not len(full_name.split(' ')) == 2:
            return False, 'Полное имя должно содержать только Фамилию и Имя.'

        # Проверка наличия пробелов в имени
        if ' ' not in full_name:
            return False, 'Полное имя должно содержать пробелы.'
        
        # Проверка наличия символа '.' в имени
        if '.' in full_name:
            return False, 'Полное имя не должно содержать символ ".".'
        
        # Проверка наличия символа '-' в имени
        if '-' in full_name:
            return False, 'Полное имя не должно содержать символ "-".'
        
        return True, "Полное имя валидно"

    except Exception as e:
        return False, str(e)

def password_is_valid(password: str):
    """
    Валидация пароля
    """

    # Проверка длины пароля
    if len(password) < 6:
        return False, 'Пароль должен содержать минимум 6 символов.'
    
    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        return False, 'Пароль должен содержать хотя бы одну заглавную букву.'
    
    # Проверка наличия хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        return False, 'Пароль должен содержать хотя бы одну строчную букву.'
    
    # Проверка наличия хотя бы одной цифры
    if not re.search(r'\d', password):
        return False, 'Пароль должен содержать хотя бы одну цифру.'
    
    # Проверка наличия хотя бы одного специального символа
    special_chars = r'[\W_]'
    if not re.search(special_chars, password):
        return False, 'Пароль должен содержать хотя бы один специальный символ.'
    
    # Пароль соответствует всем условиям
    return True, 'Пароль валиден.'



"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""