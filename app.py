from flask import Flask
from config import Config
from models.models import db, User
from flask_login import LoginManager

from routes.auth import auth
from routes.employee import employee
from routes.admin import admin

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

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

@app.route("/")
def home():
    return "<h2>Cloud Intrusion Detection using Honeytokens</h2><br><a href='/login'>Login</a>"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)