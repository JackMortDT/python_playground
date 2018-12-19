from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'LuisSas'}
    songs = [
        {
            'author': {'username': 'The Cat Empire'},
            'body': 'The wine song'
        },
        {
            'author': {'username': 'Muse'},
            'body': 'Hysteria'
        }
    ]
    return render_template('index.html', title='Home', user=user, songs=songs)
