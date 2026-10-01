from flask import Flask, render_template
from config import Config
from models.models import db, User
from flask_login import LoginManager

from routes.auth import auth
from routes.employee import employee
from routes.admin import admin
from routes.security import security
from routes.incidents import incidents
from routes.reports import reports


app = Flask(__name__)
app.config.from_object(Config)


# Database
db.init_app(app)


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(employee)
app.register_blueprint(admin)
app.register_blueprint(security)
app.register_blueprint(incidents)
app.register_blueprint(reports)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Create database tables
with app.app_context():
    db.create_all()


# Run application
if __name__ == "__main__":
    app.run(debug=True)