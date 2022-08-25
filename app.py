
# from crypt import methods
# from enum import unique
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String


# basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/dict'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


# metadata_obj = MetaData()

# user = Table(
#     'user',
#     metadata_obj,
#     Column('user_id', Integer, primary_key=True),
#     Column('user_name', String(16), nullable=False),
#     Column('email_address', String(60)),
#     Column('nickname', String(50), nullable=False)
# )


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
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        chi=request.form["chi"]
        eng=request.form["eng"]
        pinyin=request.form["pinyin"]
        # file=request.files["file"]
        # file.save(secure_filename("uploaded"+file.filename))
        # with open("uploaded"+file.filename,"a") as f:
        # f.write("This was added later!")
        # print(type(file))
        
        # --- TEST WRITING CONDITIONAL , step by step
        # print(chi,eng,pinyin)
        # print(request.form)
        # print(db.session.query(Data).filter(Data.chi_==chi))
        # print(db.session.query(Data).filter(Data.chi_==chi).count())
        
        # for item in range:
        #     range = db.session.query(Data).filter(Data.chi_==chi)
        #     print(item)
            
        # check if unique,
        if db.session.query(Data).filter(Data.chi_==chi).count() == 0:
            data=Data(chi,eng,pinyin)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template("index.html", text="word already exists")


result_set = db.session.query("SELECT * FROM data")  
for r in result_set:  
    print(r)


# @app.route("/pinyin")
# , methods=['GET']
# def pinyin():
#     # data=Data(pinyin)
#     data = Data.query.filter_by(Data.pinyin_==pinyin).all()
#     return f'{data.pinyin_}'
    
# @app.route("/english.html", methods=['GET'])
    # def english():


# print(db.session.query(Data).filter(Data.chi_==chi))


if __name__ == '__main__':
    app.debug=True
    app.run()

