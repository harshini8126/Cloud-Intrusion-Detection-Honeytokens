from flask import Blueprint, render_template
from flask_login import login_required
from models.models import Log, Alert, Incident

reports = Blueprint("reports", __name__)


@reports.route("/security/reports")
@login_required
def security_reports():
    total_access_events = Log.query.count()
    honeytoken_incidents = Log.query.filter_by(status="Honeytoken Access").count()
    normal_accesses = Log.query.filter_by(status="Normal Access").count()

    total_incidents = Incident.query.count()
    resolved_incidents = Incident.query.filter_by(status="RESOLVED").count()
    unresolved_incidents = total_incidents - resolved_incidents

    return render_template(
        "reports.html",
        total_access_events=total_access_events,
        honeytoken_incidents=honeytoken_incidents,
        normal_accesses=normal_accesses,
        total_incidents=total_incidents,
        resolved_incidents=resolved_incidents,
        unresolved_incidents=unresolved_incidents,
    )