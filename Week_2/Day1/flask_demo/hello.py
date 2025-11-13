from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/square/<num>')
def square_num(num):
    n = int(num)
    return "%d" % (n ** 2)

@app.route('/circle/<rad_num>')
def circle_rad(rad_num):
    x = float(rad_num)
    return f"{x * 2}"

@app.route('/sum/<num_1>/<num_2>')
def sum_of_nums(num_1, num_2):
    return str(float(num_1) + float(num_2))

@app.route('/hello')
def hello_again():
    return 'Hello World Again'

@app.route('/hello/<name>')
def hiname(name):
    return f"Hi, {name}!"

@app.route('/admin')
def hello_admin():
    return "Hello ADMIN"

@app.route('/user/<name>')
def hello_user(name):
    if name.lower() == "admin":  # ✅ correct
        return redirect(url_for('hello_admin'))
    else:
        return f"Hello, Guest: {name}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form['nm']
    return f"Form Processing... Hello, {name}!"








def hithere():
    return 'hi there'

app.add_url_rule('/hi', view_func=hithere)

if __name__ == '__main__':
    app.run(debug=True)
