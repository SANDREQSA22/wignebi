from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"id": 2, "title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"id": 3, "title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877},
    {"id": 4, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880},
    {"id": 5, "title": "The Master and Margarita", "author": "Mikhail Bulgakov", "year": 1967},
    {"id": 6, "title": "The Maltese Falcon", "author": "Dashiell Hammett", "year": 1930},
    {"id": 7, "title": "The Hound of the Baskervilles", "author": "Arthur Conan Doyle", "year": 1902},
    {"id": 8, "title": "Murder on the Orient Express", "author": "Agatha Christie", "year": 1934},
    {"id": 9, "title": "The Big Sleep", "author": "Raymond Chandler", "year": 1939},
    {"id": 10, "title": "Gone Girl", "author": "Gillian Flynn", "year": 2012},
    {"id": 11, "title": "Mozart: A Life", "author": "Maynard Solomon", "year": 1995},
    {"id": 12, "title": "Beethoven: Anguish and Triumph", "author": "Jan Swafford", "year": 2014},
    {"id": 13, "title": "The Rest Is Noise: Listening to the Twentieth Century", "author": "Alex Ross", "year": 2007},
    {"id": 14, "title": "How Music Works", "author": "David Byrne", "year": 2012},
    {"id": 15, "title": "Born to Run", "author": "Bruce Springsteen", "year": 2016}
]



@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    for book in books:
        if book['id'] == book_id:
            return render_template('book.html', book=book)
    return 'Book not found', 404


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "title": request.form['title'],
            "author": request.form['author'],
            "year": int(request.form['year'])
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)