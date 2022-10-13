from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', name = "sam")

@app.route("/blogs")
def blogs():
    return "<p>No blogs so far!</p>"

app.run(debug=True)