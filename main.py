from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':
            return f"Welcome, {username}! You are logged in."
        else:
            error = "Invalid credentials. Try again."
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
