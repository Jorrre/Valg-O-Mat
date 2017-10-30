# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import json
import random
app = Flask(__name__)

with open('./static/data.json') as data:
    j = json.load(data)

# Variables
answers = []
rankings = [0, 0, 0, 0, 0, 0]

g = 0
qt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(qt)

varBtn = "Neste"

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
    print(g)
    print(len(request.form['input']))

    if len(request.form['input']) > 1:
        if request.form['sender'] == 'NEXT':
            if g > 9:
                return render_template('done.html', rankings=rankings)
            else:
                g += 1
                if request.method == 'POST':
                    y = qt[g]
                    if g == 9:
                        return render_template('slides.html', question=j['spm'][y]['q'], varBtn = "Fullfør")
                    else:
                        return render_template('slides.html', question=j['spm'][y]['q'], varBtn = "Neste Spørsmål")
    else:
        return "NOOOOO" #eller "Du må velge et av alternativene"

if __name__ == "__main__":
    app.run()
