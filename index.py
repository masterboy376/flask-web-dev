from flask import Flask, render_template, request, jsonify
import db
from datetime import date
# from flask_mail import Mail

app = Flask(__name__)

@app.route("/")
def home():
    blogs = db.db.posts.find().limit(db.params["no_of_posts"])
    print(date.today())
    return render_template('index.html', params=db.params, blogs=blogs)
    
@app.route("/about")
def about():
    return render_template('about.html', params=db.params)

@app.route("/post/<string:slug>")
def post(slug):
    blog = db.db.posts.find_one({"slug":slug})
    return render_template('post.html', params=db.params, blog=blog)

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