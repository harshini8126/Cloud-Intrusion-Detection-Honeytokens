from flask import Flask, render_template
from routes.security import security, add_log

app = Flask(__name__)

app.register_blueprint(security)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/folder/<folder_name>")
def folder(folder_name):

    honeytoken_folders = ["Admin_Backup", "CEO_Private"]

    if folder_name in honeytoken_folders:

        add_log(
            "employee",
            folder_name,
            "Honeytoken Access"
        )

        return render_template(
            "folder.html",
            folder=folder_name,
            alert=True,
            folder_type="Honeytoken"
        )

    else:

        add_log(
            "employee",
            folder_name,
            "Normal Access"
        )

        return render_template(
            "folder.html",
            folder=folder_name,
            alert=False,
            folder_type="Normal"
        )


if __name__ == "__main__":
    app.run(debug=True)