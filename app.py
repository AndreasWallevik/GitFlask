from flask import Flask, render_template, redirect, session
from helpers import shuffle_word
from helpers.shuffle_word import get_shuffled_word

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/andreas', methods=['POST'])
def shuffle():
    return render_template('andreas.html', word=get_shuffled_word())

@app.route("/anders")
def anders():
    return render_template("anders.html")

if __name__ == '__main__':
    app.run(debug=True)
