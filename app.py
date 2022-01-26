from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)



class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anime = db.Column(db.String,nullable=False)
    image = db.Column(db.String, nullable=False)

    def toDict(self):
      return {
        "id": self.id,
        "anime": self.anime,
        "image": self.image,
      }




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello matthew"

if __name__=="__main__":
    app.run(debug=True)