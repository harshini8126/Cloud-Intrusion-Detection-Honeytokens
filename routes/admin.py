from flask import Blueprint, render_template
from flask_login import login_required

from models.models import Log, Alert

admin = Blueprint("admin", __name__)


@admin.route("/admin")
@login_required
def admin_dashboard():

    logs = Log.query.order_by(Log.id.desc()).all()
    alerts = Alert.query.order_by(Alert.id.desc()).all()

    return render_template(
        "admin.html",
        logs=logs,
        alerts=alerts
    )