from flask import *
from flask import request
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)


app.debug = True
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'user@gmail.com'
app.config['MAIL_PASSWORD'] = 'password;'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/hobbies')
def hobbies():
	return render_template('hobbies.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method=='POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']
		msg = Message(message, sender=email, recipients=["jordanch@umich.edu"])
		msg.body = "This is the email body"
		mail.send(msg)
	return render_template('contact.html')

if __name__=='__main__':
	app.run()

