import os

class Config:
    SECRET_KEY = "cloud_intrusion_secret_key"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "cloud.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False