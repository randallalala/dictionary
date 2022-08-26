# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from show_results import show_results

# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/dict'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)

# class Data(db.Model):
#     __tablename__="data"
#     id=db.Column(db.Integer, primary_key=True)
#     # underscore to discriminate
#     chi_=db.Column(db.String, unique=True)
#     eng_=db.Column(db.String, unique=True)
#     pinyin_=db.Column(db.String, unique=True)
    
#     def __init__(self, chi_, eng_, pinyin_):
#         self.chi_=chi_
#         self.eng_=eng_
#         self.pinyin_=pinyin_
        
# def show_results(chi,eng,pinyin):
#     chi=request.form["chi"]
#     # eng=request.form["eng"]
#     # pinyin=request.form["pinyin"]
#     # print()
#     print(db.session.query(Data).filter(Data.chi_==chi))
        