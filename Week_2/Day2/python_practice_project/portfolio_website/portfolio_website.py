"""
Requirements:

    Build a simple personal portfolio with Flask.
    Have pages like Home,Projects, and Contact.
    Load project data from a JSON file.

"""

import json
from flask import Flask, render_template

#flask setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return("Hello World!")

@app.route('/projects')
def projects():
    with open("project_data.json") as f:
        data = json.load(f)
        return("We are in the projects page!")

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
