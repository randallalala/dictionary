
# from crypt import methods
# from enum import unique
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, text

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/dict'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    # underscore to discriminate
    chi_=db.Column(db.String, unique=True)
    eng_=db.Column(db.String, unique=True)
    pinyin_=db.Column(db.String, unique=True)
    
    def __init__(self, chi_, eng_, pinyin_):
        self.chi_=chi_
        self.eng_=eng_
        self.pinyin_=pinyin_
    
from app import db, Data

@app.route("/")
def index():
    words = Data.query.all()
    return render_template("index.html", content=words)

# words = Data.query.all()
# for word in words:
    # print(word.pinyin_)
    # print(word.chi_)
    # print(word.eng_)

# sorted = Data.query.order_by().all()
# words = Data.query.all()
# for word in words:
#     print(Data.query(pinyin_).order_by().all())
    # print(word.chi_)
    # print(word.eng_)

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        chi=request.form["chi"]
        eng=request.form["eng"]
        pinyin=request.form["pinyin"]
        
        # --- TEST WRITING CONDITIONAL , step by step
        # print(chi,eng,pinyin)
        # print(request.form)
        # print(db.session.query(Data).filter(Data.chi_==chi))
        # print(db.session.query(Data).filter(Data.chi_==chi).count())
        
        # check if unique,
        if db.session.query(Data).filter(Data.chi_==chi).count() == 0:
            data=Data(chi,eng,pinyin)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template("index.html", text="word already exists")



if __name__ == '__main__':
    app.debug=True
    app.run()

