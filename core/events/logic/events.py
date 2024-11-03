from models.models import Event, User
from sqlalchemy.orm import Session
from models.config import engine
from datetime import datetime
from sqlalchemy import select


def create_event(request):
    response ={}
    title, photo, date, user_id = parse(request)
    try:
        with Session(engine) as session:
            new_event =Event(title=title,
            photo=photo,
            date=date,
            user_id=user_id)
            session.add(new_event)
            session.commit()
        response['status'] = 200
    except Exception as error:
        response['status'] = 400
        print(error)
    return response 

def parse(request):
    title=request.data['title']
    photo=request.FILES['photo'].read()
    date=datetime.strptime(request.data['date'], '%Y-%m-%d').date()
    with Session(engine) as session:
        user = select(User).where(User.username == request.data['user_id'])
        user_id = session.scalar(user).id
    return title, photo, date, user_id