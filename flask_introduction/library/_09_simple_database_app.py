"""HTML generated from data pulled from a database.

In this example we're pulling data from a simple sqlite3 database and
building an HTML template with it.

Requirements:
 * A database created with some data about books inside.
"""
import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.route('/')
def hello_world():
    db_connection = connect_db()
    cursor = db_connection.execute('SELECT id, title FROM book;')
    books = [dict(id=row[0], title=row[1]) for row in cursor.fetchall()]
    #send books object into the template and render the data as HTML
    return render_template('database/books_template_engine.html', books=books)
