from app import app
from models.models import db, User
from werkzeug.security import generate_password_hash

with app.app_context():

    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)

    if not User.query.filter_by(username="employee").first():
        employee = User(
            username="employee",
            password=generate_password_hash("emp123"),
            role="employee"
        )
        db.session.add(employee)

    db.session.commit()
    print("Users created successfully!")