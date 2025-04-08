from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Potrzebne do przechowywania sesji (np. flash messages)

# Statyczne dane logowania (na razie tylko dla testów)
USER_CREDENTIALS = {'username': 'admin', 'password': 'password'}

# Tymczasowy "magazyn" na wiadomości kontaktowe
contact_messages = []

@app.route('/')
def homepage():
    return render_template('index.html')  # Strona główna z komunikatami flash

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        if not name or not message:
            flash('Please fill in all fields.', 'danger')
            return redirect(url_for('contact'))

        # Dodanie wiadomości do kontaktu
        contact_messages.append({'name': name, 'message': message})
        
        flash(f'Thank you for your message, {name}!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/messages')
def messages():
    return render_template('messages.html', messages=contact_messages)

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

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
        else:
            # Zaktualizuj hasło użytkownika (na razie tylko w pamięci)
            USER_CREDENTIALS['password'] = new_password
            flash('Password changed successfully!', 'success')
            return redirect(url_for('homepage'))

    return render_template('change_password.html')

if __name__ == '__main__':
    app.run(debug=True)