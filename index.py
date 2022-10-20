from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/postContact")
def postContact():
    db.db.posts.insert_one({"name": "John"})
    return "Connected to the data base!"

app.run(debug=True)