# server/seed.py

from models import db, Author, Post
from app import app  # Make sure your Flask app instance is in app.py

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create some authors
    author1 = Author(name="Alice Johnson", phone="1234567890")
    author2 = Author(name="Bob Smith", phone="0987654321")

    db.session.add_all([author1, author2])
    db.session.commit()

    # Create some posts
    post1 = Post(
        title="You Won't Believe What Happened Next!",
        content="A" * 300,  # At least 250 characters
        summary="An exciting post summary",
        category="Fiction",
        author_id=author1.id
    )

    post2 = Post(
        title="Top 10 Secrets You Must Know",
        content="B" * 300,
        summary="Short summary",
        category="Non-Fiction",
        author_id=author2.id
    )

    db.session.add_all([post1, post2])
    db.session.commit()

    print("Database seeded successfully!")
