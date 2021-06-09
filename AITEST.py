from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1qaz2wsx@127.0.0.1:3308/ai_auto_inference"
db.init_app(app)

class User(db.Model):
    id= db.Column(db.Interger, primary_key=True)
    process= db.Column(db.String(10))
    study_id= db.Column(db.Integer)

    def __init__(self, process, study_id):
        self.process = process
        self.study_id = study_id

    def __repr__(self):
        return '<User %s>' % self.process

@app.route('/show/<process>')
def show(process):
    user = User.query.filter_by(process=process).first()
    return f"{process} study:{user.study_id}
