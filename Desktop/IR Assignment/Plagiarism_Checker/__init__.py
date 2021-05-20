from flask import Flask

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['SECRET_KEY']= '9c843bca4be83a99a18cb1d1'
app.config['UPLOAD_FOLDER']='./Plagiarism_Checker/Docs'

from Plagiarism_Checker import routes
