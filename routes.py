import os
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/features')
def features():
	return render_template('Features.html')

@app.route('/donate')
def donate():
	return render_template('donate.html')

@app.route('/campaign')
def campaign():
	return render_template('campaign.html')

@app.route('/gifts')
def gifts():
	return render_template('gifts.html')

@app.route('/profile')
def profiles():
	return render_template('profile.html')

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)