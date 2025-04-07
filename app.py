from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to the homepage'

@app.route('/contact', methods=['POST'])
def contact():
    return 'Thank you for your message!'

@app.route('/about')
def about():
    return "This is a simple DevOps demo app."

if __name__ == '__main__':
    app.run(debug=True)