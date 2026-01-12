from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)

    def __init__(self, name, phone_number):
        # Name required
        if not name:
            raise ValueError("Author must have a name")

        # Phone number length
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 10 digits")

        # Unique name check
        existing_author = Author.query.filter_by(name=name).first()
        if existing_author:
            raise ValueError("Author name must be unique")

        self.name = name
        self.phone_number = phone_number


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String, nullable=False)

    def __init__(self, title, content, category, summary=""):
        # Title required
        if not title:
            raise ValueError("Post must have a title")

        # Clickbait check
        clickbait_keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(keyword in title for keyword in clickbait_keywords):
            raise ValueError("Post title is not clickbait-y enough")

        # Content length
        if len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long")

        # Summary length
        if len(summary) > 250:
            raise ValueError("Post summary cannot exceed 250 characters")

        # Category check
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Post category must be either 'Fiction' or 'Non-Fiction'")

        self.title = title
        self.content = content
        self.category = category
        self.summary = summary
