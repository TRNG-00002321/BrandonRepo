"""
Requirements:

    Build a simple personal portfolio with Flask.
    Have pages like Home,Projects, and Contact.
    Load project data from a JSON file.

"""

import json
from flask import Flask, render_template, url_for

#flask setup
app = Flask(__name__)


#Home page
@app.route('/')
def hello_world():

    #in home, i need a button that takes you to projects and contact page
    return render_template("home.html")

@app.route('/projects')
def projects():
    with open("project_data.json") as f:
        data = json.load(f)

        project_data = {}
        for item in data:
            if(item["page"] == "Projects"):
                project_data = item
                break

        return render_template("projects.html", data=project_data)

@app.route('/contact')
def contact():
    with open("project_data.json") as f:
        data = json.load(f)

    contact_data = {}
    for item in data:
        if item["page"] == "Contact":
            contact_data = item
            break

    return render_template("contact.html", data=contact_data)

if __name__ == "__main__":
    app.run(debug=True)
