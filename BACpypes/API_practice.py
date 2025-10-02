from flask import Flask, jsonify, request, redirect, url_for, render_template, flash

app = Flask(__name__)

devices = [
    {"id": 1, "name": "Thermostat", "status": "online"},
    {"id": 2, "name": "Light Sensor", "status": "offline"},
    {"id": 3, "name": "Test", "status": "NIL"},
    ]

@app.route('/')
def home():
    txt = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to My Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
            padding: 50px;
        }
        img {
            width: 600px;
            border-radius: 10px;
            box-shadow: 0 0 10px #aaa;
        }
    </style>
</head>
<body>
    <h1>Hello, Ujjwal!</h1>
    <p>Here's a beautiful view of the Taj Mahal:</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/1d/Taj_Mahal_%28Edited%29.jpeg" alt="Taj Mahal">
</body>
</html>'''
    #flash('this is an alert')
    return txt

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID): 
    return 'Blog Number %d' % postID  

@app.route('/rev/<float:revNo>')
def revision(revNo): 
    return 'Revision Number %f' % revNo

@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
    
@app.route("/index")
def index():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)