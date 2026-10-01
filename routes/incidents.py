from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models.models import db, Log, Alert, Incident

incidents = Blueprint("incidents", __name__)


@incidents.route("/incidents")
@login_required
def incident_list():

    if current_user.role != "admin":
        return redirect(url_for("employee.dashboard"))

    logs = Log.query.order_by(Log.id.desc()).all()
    alerts = Alert.query.order_by(Alert.id.desc()).all()

    for alert in alerts:
        existing = Incident.query.filter_by(alert_id=alert.id).first()

        if not existing:
            related_log = Log.query.filter_by(
                username=alert.username,
                status="Honeytoken Access"
            ).order_by(Log.id.desc()).first()

            resource = related_log.folder_name if related_log else "Unknown Resource"
            event_time = related_log.access_time if related_log else alert.alert_time

            incident = Incident(
                alert_id=alert.id,
                username=alert.username,
                resource=resource,
                event_type="Honeytoken Access",
                event_time=event_time,
                severity="HIGH",
                status="NEW"
            )

            db.session.add(incident)

    db.session.commit()

    incidents_list = Incident.query.order_by(Incident.id.desc()).all()

    return render_template(
        "incidents.html",
        logs=logs,
        alerts=alerts,
        incidents=incidents_list
    )


@incidents.route("/incidents/update/<int:incident_id>/<status>")
@login_required
def update_incident(incident_id, status):

    if current_user.role != "admin":
        return redirect(url_for("employee.dashboard"))

    incident = Incident.query.get_or_404(incident_id)

    if status in ["NEW", "INVESTIGATING", "RESOLVED"]:
        incident.status = status
        db.session.commit()

    return redirect(url_for("incidents.incident_list"))