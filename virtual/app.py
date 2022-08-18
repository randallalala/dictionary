
from crypt import methods
from enum import unique
# import pywebio
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# from pywebio.input import input, TEXT
# from pywebio.output import put_text, put_html, put_markdown, put_table

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/dict'
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
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def sucess():
  if request.method=='POST':
        file=request.files["file"]
        # file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename,"a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html", btn="download.html")


if __name__ == "__main__":
    debug=True
    app.run()

# ----------------------------------------------------------------------------- 

# def bmi():
#     eng = input("eng:", type=TEXT) 
#     chi = input("chi:", type=TEXT)

#             # put_markdown('# **Results**')
#             # put_text('eng: %.1f' % ( status))
#             # put_html('<br><br>')
#             # # put_markdown('Your BMI: `%.1f` ' % ( status))
#             # put_html('<hr>')
#     put_table([
#         ['ENG', 'CHI'],
#         [eng , chi],
#     ])

# if __name__ == '__main__':
#     pywebio.start_server(bmi, port=55)