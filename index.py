from flask import Flask, render_template, request, jsonify
import db
from datetime import date
from flask_mail import Mail

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = db.params['gmail_username'],
    MAIL_PASSWORD = db.params['gmail_password']
)

mail = Mail(app);

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
        mail.send_message('New message from: '+name+' on Blog Blaze',
                            sender=email,
                            recipients=[db.params['gmail_username']],
                            body=message+'\n phone:'+phone)
    return render_template('contact.html', params=db.params)


app.run(debug=True)