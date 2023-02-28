from models import User

user = User.query.first()
print(
    f"""Имя {user.name}
Зарплата {user.salary}
Email {user.email}
"""
)
