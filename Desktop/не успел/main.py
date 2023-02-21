import random
from random import randint
from faker import Faker
from flask import (
    Flask, 
    Request, 
    Response, 
    render_template)

from flask.app import Flask as FlaskApp

from models.book import(
    Book
)

app: FlaskApp = Flask(__name__)
books: list[Book] = []
fake = Faker()
@app.route('/')
def main_page():
    return render_template(
        template_name_or_list='index.html',
        books = enumerate(books)
    )
if __name__ == '__main__':
    lii: list[dict] = []
    for _ in range(1000):
        book = Book(
        title = str(fake.name()), 
        description = str(fake.text()), 
        list_count = int(random.randint(100,1000)), 
        price = round(random.random() * 500 + 500, 2),
        rate_list=[
                random.randint(1, 10) 
                for _ in range(random.randint(1, 10))
            ]
        )
        books.append(book)

    app.run(
        host = 'localhost',
        port = 8080,
        debug = True
    )

@app.route('/{{i}}')
def dop_page():
    return render_template(
        book = book,
        template_name_or_list='dop.html'
        )