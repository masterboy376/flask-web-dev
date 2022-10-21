from flask import Flask, render_template, request, jsonify
import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', params=db.params)
    
@app.route("/about")
def about():
    return render_template('about.html', params=db.params)

@app.route("/post")
def post():
    return render_template('post.html', params=db.params)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db.db.queries.insert_one({"name": name, "email": email, "phone": phone, "message": message})
    return render_template('contact.html', params=db.params)


app.run(debug=True)