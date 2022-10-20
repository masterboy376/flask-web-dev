from flask import Flask, render_template, request, jsonify
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

@app.route("/postContact", methods=['POST'])
def postContact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db.db.queries.insert_one({"name": name, "email": email, "phone": phone, "message": message})

app.run(debug=True)