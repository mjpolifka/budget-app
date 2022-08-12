from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f'sqlite:///database.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy()
db.init_app(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # transaction_date = 
    payee = db.Column(db.String)
    description = db.Column(db.String)
    amount = db.Column(db.Float)

@app.route("/")
def index():
    return "hello world"

with app.app_context():
    print("dropping db")
    db.drop_all()
    print("building db")
    db.create_all()

    print("new transaction:")
    t = Transaction(payee='test payee', description='test description', amount=1.0)
    print(t.description)