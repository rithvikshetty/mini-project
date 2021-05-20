import os
from Plagiarism_Checker import app
from flask import render_template,redirect,request,url_for
from Plagiarism_Checker.similar_files import similar_Files

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route("/process", methods=['POST'])
def process_upload():
    file = request.files['inputfile']
    #threshold = request.form['threshold']
    #if threshold==0:
    #    threshold=10
    if file.filename == '':
        return redirect(url_for('upload_page'))
    file.filename = 'query.txt'
    if file :#and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    a = similar_Files(app.config['UPLOAD_FOLDER'])
    result,nos = a.start_sim()
    return render_template('results.html',result=result,nos=nos)#threshold = threshold

@app.route("/display_text",methods=['POST'])
def display_sim_text():
    doc = request.form['docs']
    with open(os.path.join(os.getcwd(),"Plagiarism_Checker/Docs/"+doc),"rb") as rf:
        text = rf.read()
    #text = text.rstrip("\n").decode("UTF-16")
    #text = text.split("\r\n")
    text = "".join(map(chr,text))    
    return render_template('display.html',name=doc,text=text)