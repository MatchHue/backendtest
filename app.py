from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello')
def hello():
    return "Hello matthew"

if __name__=="__main__":
    app.run(debug=True)