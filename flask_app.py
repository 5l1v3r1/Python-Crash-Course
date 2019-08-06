from flask import Flask

app = Flask(__name__)

@app.route('/')
def sayHello(name):
    print("Hello " + name + "!")
sayHello("Jason")

@app.route('/newquote')
def newQuote():
    return render_template('newQuotes.html')