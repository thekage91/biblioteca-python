from flask import Blueprint, render_template, request

Auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

@Auth.route('/signup')
def signup():
    return render_template('signup.html')

@Auth.route('/login')
def login():
    return render_template('login.html')   

@Auth.route('/forgot-password') 
def forgot_password():
    return render_template('forgot_password.html') 

@Auth.route('/register', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    return f'Email: {email}, Password: {password}'
