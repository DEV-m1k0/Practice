
import requests

def get_image_by_url(url) -> bytes:
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    return None


def load_image(image):
    return image.read()


"""

# NOTE - =========================== О разработчиках ===========================

Данный гайд был создан для того, чтобы помочь начинающим разработчикам
в создании API с использованием Django Rest Framework.

GitHub'ы разработчиков данного гайда:
 - https://github.com/DEV-m1k0
 - https://github.com/Artem822

"""