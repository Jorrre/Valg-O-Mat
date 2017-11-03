# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from methods import result
import json
import random
import io
app = Flask(__name__)

encoding = io.open('./static/data.json', 'r')
file_content = encoding.read()
file_content = file_content.replace('Ã¥', 'å')
file_content = file_content.replace('Ã¸', 'ø')
file_content = file_content.replace('Ã˜', 'Ø')
file_content = file_content.replace('Ã¦', 'æ')

j = json.loads(file_content)

# Variables
answers = []
winners_alt = []
g = 0

@app.route('/')
@app.route('/<page>')
def index(page=None):
    if page == None:
        reset()
        return render_template('index.html')
    else:
        return render_template('slides.html', question=j['spm'][0]['q'], varBtn="Neste Spørsmål")

@app.route('/next', methods=['GET', 'POST'])
def next():
    global g
    global answers
    global winners_alt
    answers.append(request.form['input'])

    if request.form['sender'] == 'NEXT':
        if g == len(j['spm'])-1:
            result(answers, j, winners_alt)
            return render_template('done.html', rankings=winners_alt)
        else:
            g += 1

            if request.method == 'POST':
                if g == len(j['spm'])-2:
                    return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Fullfør")
                else:
                    return render_template('slides.html', question=j['spm'][g]['q'], varBtn = "Neste Spørsmål")

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    reset()

    # Returning user to the startpage
    return render_template('index.html')

def reset():
    # Resetting all variables
    global g
    global answers
    global winners_alt
    g = 0
    del answers[:]
    del winners_alt[:]

if __name__ == "__main__":
    app.debug = True
    app.run()
