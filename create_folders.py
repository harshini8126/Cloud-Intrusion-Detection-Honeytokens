from app import app
from models.models import db, Folder

with app.app_context():

    folders = [
        Folder(folder_name="Documents", is_honeytoken=False),
        Folder(folder_name="Projects", is_honeytoken=False),
        Folder(folder_name="HR", is_honeytoken=False),
        Folder(folder_name="Finance", is_honeytoken=True),
        Folder(folder_name="Payroll", is_honeytoken=True),
        Folder(folder_name="Reports", is_honeytoken=False)
    ]

    for folder in folders:
        if not Folder.query.filter_by(folder_name=folder.folder_name).first():
            db.session.add(folder)

    db.session.commit()

    print("Folders created successfully!")