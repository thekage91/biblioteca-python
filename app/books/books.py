from flask import Blueprint, render_template, request, redirect, url_for
from tinydb import TinyDB

from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from tinydb import Query


#### 

class AddBookForm(FlaskForm):
    """
    Form per aggiungere un libro
    """
    title = StringField('Titolo del libro:', validators=[DataRequired()])
    author = StringField('Autore del libro', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Aggiungi libro')
    
def add_book(db, isbn, title, author):
     db.insert({
        'isbn': isbn,
        'title': title,
        'author': author,
        'status': 'available'
    })      

def remove_book_by_isbn(db, isbn):
    Book = Query()
    db.remove(Book.isbn == isbn)
    
def remove_book_by_title(db, title):
    Book = Query()
    db.remove(Book.title == title)

def get_all_books(db):
    return db.all()

def get_book(db, isbn):
    Book = Query()
    return db.search(Book.isbn == isbn)

def search_book_by_title(db, title):
    Book = Query()
    return db.search(Book.title == title)

####

Book = Blueprint('books', __name__, template_folder='templates', url_prefix='/book')

db = TinyDB('./database/db.json')

@Book.route('/home')
def home():
    books = get_all_books(db)
    return render_template('home.html', books=books)

@Book.route('/add', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        add_book(db, form.isbn.data, form.title.data, form.author.data)
        return redirect(url_for('home'))
        
    return render_template('add_book.html',form=form)

@Book.route('/<isbn>')
def book(isbn):
    book = get_book(isbn)
    return render_template('book.html', book=book)

@Book.route('/remove/<isbn>', methods=['POST'])
def remove_book(isbn):
    return redirect(url_for('home'))

@Book.route('/search-by-title', methods=['POST'])
def remove_book_by_title():
    title = request.form.get('title')
    remove_book_by_title(db, title)
    return redirect(url_for('home'))

url_for('books.remove_book_by_title')