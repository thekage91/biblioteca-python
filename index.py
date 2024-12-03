from flask import Flask

from app.auth import auth
from app.books import books
from app.users import users

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'una chiave segreta' 

app.register_blueprint(auth.Auth) 
app.register_blueprint(books.Book)
app.register_blueprint(users.Users)

print('Applicazione avviata')
print('Ciao mondo')
print('Ciao mondo 2')

if __name__ == '__main__':
    app.run(debug=True)