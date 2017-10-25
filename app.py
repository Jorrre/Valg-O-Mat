# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

with open('static/data.json') as f:
    a = json.load(f)

# Variables
answers = []
g = 0

@app.route('/')
@app.route('/<page>')
def main(page=None):
    if page == None:
        return render_template('index.html')
    else:
        return render_template('slides.html', question=a['spm'][0]['q'])

@app.route('/next', methods=['GET', 'POST'])
def next():
    global g
    if request.form['sender'] == 'NEXT':
        # Next Question
        if g == 10:
            render_template('done.html')
        else:
            g += 1
            if request.method == 'POST':
                return render_template('slides.html', question=a['spm'][g]['q'], counter=g)

@app.route('/done', methods=['GET', 'POST'])
def done():
    '''
        Her må vekttabellene legges sammen
        og resultatene må indekseres.
    '''
    return render_template('done.html')

if __name__ == "__main__":
    app.run()
