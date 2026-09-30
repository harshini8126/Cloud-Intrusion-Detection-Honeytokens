from flask import Blueprint, render_template
from datetime import datetime


security = Blueprint("security", __name__)


logs = []
alerts = []


def add_log(username, folder, status):

    log = {
        "username": username,
        "folder": folder,
        "status": status,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    logs.append(log)

    if status == "Honeytoken Access":

        alert = {
            "username": username,
            "message": f"Honeytoken accessed: {folder}",
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        alerts.append(alert)


@security.route("/security")
def security_dashboard():

    return render_template(
        "security.html",
        logs=logs,
        alerts=alerts
    )
