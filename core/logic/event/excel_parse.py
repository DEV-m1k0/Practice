"""

#SECTION - ====================== Файл для парсинга данных ======================

"""

import pandas
from logic.utils.image import get_image_by_url
from models.config import session
from models.models import User
from sqlalchemy import select
from datetime import datetime
def parse_excel(excel_file):

    try:
        df = pandas.read_excel(excel_file)
        events = []
        counter = 0
        stop = len(df.values)
        for row in df.values:   
            if counter == stop:
                break


            event_dict = {}
            event_dict["title"] = row[0]
            image_url = row[1]
            event_dict["date"] = datetime.strptime(row[2], '%Y-%m-%d').date()
            user = select(User).where(User.username == row[3])
            event_dict['user_id'] = session.scalar(user).id
            

            bimage = get_image_by_url(url=image_url)
            if bimage is not None:
                event_dict["photo"] = bimage
                
            else:
                bimage = None
                event_dict["photo"] = bimage
            events.append(event_dict)
            counter += 1
            print(events)
        return events

    except ValueError as e:
        print(e)
        return "BAD_REQUEST"