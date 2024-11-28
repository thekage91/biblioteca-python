from tinydb import Query

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

def search_book_by_title(db, title):
    Book = Query()
    return db.search(Book.title == title)