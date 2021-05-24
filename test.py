from flask import Flask ,render_template ,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://kbjtcfqpgeydhm:4f6424f991fa66a3a27e91d55c5d0dc656b8d3a15763ab3e5be67904692f17db@ec2-52-50-171-4.eu-west-1.compute.amazonaws.com:5432/d13dd2d24muunr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
