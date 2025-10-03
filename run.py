from app import app
from app.models import User, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email:{user.email}")

app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
