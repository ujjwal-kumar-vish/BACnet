from flask import Flask, request, redirect, flash, render_template, url_for
app = Flask(__name__)

# /login display login form

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
    return txt


@app.route('/login', methods=['GET', 'POST'])
# login function verify username and password
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:

            # flashes on successful login
            flash('You were successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)