import os
from project import app
from flask import render_template,redirect,request,url_for
from project.LogisticRegression import LR 
from project.preprocessing import preprocess
from project.generate_report import report

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route("/process",methods=['POST'])
def process_upload():
    file = request.files['inputfile']
    model = request.form['modelname']
    #threshold = request.form['threshold']
    #if threshold==0:
    #    threshold=10
    if file.filename == '':
        return redirect(url_for('upload_page'))
    file.filename = 'test.csv'
    if file :#and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    #preprocessing
    x = preprocess()
    x.preprocessing()

    #model selection
    a = LR()
    a.LogisticRegression()

    #report
    y = report()
    y.perc_eng()
    return render_template('display.html')

@app.route('/display')
def display():
    return render_template('display.html')
