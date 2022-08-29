
# from crypt import methods
# from enum import unique
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, text, desc

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/dict'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    # underscore to discriminate
    pinyin_=db.Column(db.String, unique=True)
    eng_=db.Column(db.String, unique=True)
    chi_=db.Column(db.String, unique=True)
    
    def __init__(self, chi_, eng_, pinyin_):
        self.chi_=chi_
        self.eng_=eng_
        self.pinyin_=pinyin_
    
from app import db, Data

@app.route("/")
def home():
    # pinyin = Data.query.order_by(Data.pinyin_.asc()).all()
    # eng = Data.query.order_by(Data.eng_.asc()).all()
    # chi = Data.query.order_by(Data.chi_.asc()).all()
    content = Data.query.all()
    return render_template("home.html", content=content)

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        pinyin=request.form["pinyin"]
        eng=request.form["eng"]
        chi=request.form["chi"]
        
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
    return render_template("home.html", text="word already exists")


@app.route("/content/<int:content_id>/update", methods=['POST'])
def update_content(content_id):
    content = content.query.get_or_404(content_id)
    # form = 
    return render_template("success.html")

        
        # --- TEST WRITING CONDITIONAL , step by step
        # print(chi,eng,pinyin)


if __name__ == '__main__':
    app.debug=True
    app.run()

# TO ADD
# - edit delete
# - upload data from file
# - download backup file
# - password for delete
# - sort pinyin / english - sort button
# - other languages

# SQL QUERY
# UPDATE  data
# SET pinyin_ = 'bianliang'
# WHERE id ='8'
# RETURNING *
# ---
# SELECT * 
# FROM data
# ORDER BY chi_ DESC 
