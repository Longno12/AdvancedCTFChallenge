from flask import Flask, render_template, request, redirect, url_for
from utils.cipher import decode_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/secret')
def secret():
    secret_message = ""
    with open('hidden/hidden_message.txt', 'r') as file:
        secret_message = file.read()
    decoded_message = decode_message(secret_message)
    return render_template('secret.html', message=decoded_message)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password123':
        return redirect(url_for('secret'))
    else:
        return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
