from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from models.models import db, Folder, Log, Alert
from routes.security import add_log

employee = Blueprint("employee", __name__)


@employee.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@employee.route("/honeytoken-access", methods=["POST"])
@login_required
def honeytoken_access():

    data = request.get_json()

    if not data or "resource" not in data:
        return jsonify({
            "message": "Invalid resource request."
        }), 400

    resource_name = data["resource"]

    folder = Folder.query.filter_by(
        folder_name=resource_name
    ).first()

    if folder is None:
        return jsonify({
            "message": "Resource not found."
        }), 404

    if folder.is_honeytoken:

        log = Log(
            username=current_user.username,
            folder_name=resource_name,
            status="Honeytoken Access"
        )

        alert = Alert(
            username=current_user.username,
            alert_message=f"Suspicious resource access detected: {resource_name}"
        )

        db.session.add(log)
        db.session.add(alert)
        db.session.commit()
        add_log(current_user.username, resource_name, "Honeytoken Access")
        add_log(current_user.username, resource_name, "Honeytoken Access")

    else:

        log = Log(
            username=current_user.username,
            folder_name=resource_name,
            status="Normal Access"
        )

        db.session.add(log)
        db.session.commit()

    return jsonify({
        "message": "Resource access recorded."
    })


