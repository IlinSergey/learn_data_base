from db import db_session
from models import User

user = User(name="Мария Сидорова", salary=2222, email="msidorova@example.com")
db_session.add(user)
db_session.commit()
