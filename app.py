from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Potrzebne do przechowywania sesji (np. flash messages)

# Statyczne dane logowania (na razie tylko dla testów)
USER_CREDENTIALS = {'username': 'admin', 'password': 'password'}

@app.route('/')
def homepage():
    return 'Welcome to the homepage'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f'Thank you for your message, {name}!'
    return render_template('contact.html')

@app.route('/about')
def about():
    return "This is a simple DevOps demo app."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            flash('Login successful!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)