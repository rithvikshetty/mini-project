from flask import Flask

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['SECRET_KEY']= '9c843bca4be83a99a18cb1d1'
app.config['UPLOAD_FOLDER']='./project/docs/uploaded/data'

from project import routes