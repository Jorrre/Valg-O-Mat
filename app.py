# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from methods import result
import json
import random
app = Flask(__name__)

with open('./static/data.json') as data:
    j = json.load(data)

# Variables
answers = []
rankings = []
winners_alt = []
g = 0

@app.route('/')
@app.route('/<page>')
def index(page=None):
    if page == None:
        return render_template('index.html')
    else:
        return render_template('slides.html', question=j['spm'][0]['q'], varBtn="Neste Spørsmål")

@app.route('/next', methods=['GET', 'POST'])
def next():
    global g
    global answers
    answers.append(request.form['input'])

    if request.form['sender'] == 'NEXT':
        if g > 10:
            fuck = result(answers, j)
            return render_template('done.html', rankings=fuck)
        else:
            g += 1
            if request.method == 'POST':
                if g == 9:
                    return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Fullfør")
                else:
                    return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Neste Spørsmål")

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    # Resetting all variables
    global g
    global answers
    g = 0
    del answers[:]

    # Returning user to the startpage
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
