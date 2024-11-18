"""

#SECTION - ====================== Файл для парсинга данных ======================

"""


import pandas
from PIL import Image
from .image import get_image_by_url
from django.contrib.auth.hashers import make_password



def parse_excel(excel_file):

    try:
        df = pandas.read_excel(excel_file)
        users = []
        images_for_users = []
        counter = 0
        stop = len(df.values)

        for row in df.values:
            counter += 1
            if counter == stop:
                break

            user_dict = {}

            user_dict["id_number"] = row[0]
            user_dict["username"] = row[0]
            user_dict["password"] = make_password(row[1])
            user_dict["first_name"] = row[2]
            user_dict["last_name"] = row[3]
            user_dict["role"] = row[4]
            image_url = row[5]
            user_dict["gender"] = row[6]
            user_dict["email"] = row[7]
            user_dict["phone"] = row[8]
            user_dict["direction"] = row[9]
            user_dict["event"] = row[10]

            bimage = get_image_by_url(url=image_url)
            if bimage is not None:
                user_dict["photo"] = bimage
                
            else:
                bimage = None
                user_dict["photo"] = bimage

            users.append(user_dict)
        
        return users

    except ValueError as e:
        print(e)
        return "BAD_REQUEST"