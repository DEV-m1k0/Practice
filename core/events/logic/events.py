from models.models import Event 
from sqlalchemy.orm import Session
from models.config import engine
def create_event(request):
    response ={}
    try:
        with Session(engine) as session:
            new_event =Event(title=request.data['title'],
            photo=request.data['photo'],
            date=request.data['date'],
            user_id=request.data['user_id'])
            session.add(new_event)
            session.commit()
            session.refresh(Event)
        response['status'] = 200
    except Exception as error:
        response['status'] = 400
        print(error)
    return response 