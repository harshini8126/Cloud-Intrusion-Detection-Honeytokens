from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from models.models import db, Folder, Log, Alert

employee = Blueprint("employee", __name__)


@employee.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@employee.route("/honeytoken-access", methods=["POST"])
@login_required
def honeytoken_access():

    data = request.get_json()

    resource_name = data.get("resource")

    # Find the folder/resource
    folder = Folder.query.filter_by(folder_name=resource_name).first()

    # If the resource does not exist
    if folder is None:
        return jsonify({
            "message": "Resource not found."
        }), 404

    # Check whether it is a honeytoken
    if folder.is_honeytoken:

        # Record the suspicious access
        log = Log(
            username=current_user.username,
            folder_name=resource_name,
            status="Honeytoken Access"
        )

        # Create security alert
        alert = Alert(
            username=current_user.username,
            alert_message=f"Honeytoken accessed: {resource_name}"
        )

        db.session.add(log)
        db.session.add(alert)
        db.session.commit()

        return jsonify({
            "message": "Honeytoken accessed! Security alert generated."
        })

    # Normal resource access
    log = Log(
        username=current_user.username,
        folder_name=resource_name,
        status="Normal Access"
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({
        "message": "Resource accessed successfully."
    })