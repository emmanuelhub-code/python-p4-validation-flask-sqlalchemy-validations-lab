from app import app
from models import db, Author, Post

with app.app_context():
    db.drop_all()
    db.create_all()

    author1 = Author(name="Alice Johnson", phone_number="1234567890")
    author2 = Author(name="Bob Smith", phone_number="0987654321")

    db.session.add_all([author1, author2])
    db.session.commit()
