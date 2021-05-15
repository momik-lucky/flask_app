from flask import Flask, render_template

from utils.view_modifiers import response

app = Flask(__name__)


def get_films():
    return [
        {
            'id': 1,
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'release_date': 'November 4, 2001'
        },
        {
            'id': 2,
            'title': 'Harry Potter and Chamber of Secrets',
            'release_date': 'November 3, 2003'
        }

    ]


@app.route('/')
@app.route('/hello')
@response(template_file='hello.html')
def index():
    films = get_films()
    return {'films': films}


@app.route('/about_flowers')
def about_flowers():
    return render_template('about_flowers.html', title='About_flowers')


@app.route('/<string:name>')
def greeting(name: str):
    return f'Hello, {name.capitalize()}'


if __name__ == '__main__':
    app.run()
