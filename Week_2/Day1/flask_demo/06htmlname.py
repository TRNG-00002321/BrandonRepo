from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_world(name):
#     return render_template('helloname.html', name=name)

#@app.route('/scores/<int:score>')
#def hello_world(score):
#   return render_template('scores.html, marks=score')

@app.route('/classScores')
def student_scores():
    data = {
        "Math": 87,
        "Science": 92,
        "Physics": 99
    }

    return render_template("class_scores.html", info=data)

if __name__ == '__main__':
    app.run(debug=True)


