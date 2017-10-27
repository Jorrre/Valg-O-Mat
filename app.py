# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import json
import random
app = Flask(__name__)

with open('./static/data.json') as data:
    j = json.load(data)

# Variables
answers = []
rankings = [
    "Du bør kanskje vurdere en annen studierettning.",
    "Elektrofag med studiekompetanse ser ut til å passe for deg!",
    "Maske og hår passer fint for deg! Snakk med Åse fra Westerdals! Hilsen Oberst Tonmäster Herland!"
]

g = 0
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
                    if g == 9:
                        return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Fullfør")
                    else:
                        return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Neste Spørsmål")
    else:
        return "NOOOOO"

if __name__ == "__main__":
    app.run()
