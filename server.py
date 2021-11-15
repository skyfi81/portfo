################ WEB SERVER CREATION  ########################### build webserver with Flask(below) or Django
# first create your webserver directory, then go back one directory and run these commands in your terminal:
# 'python3 -m venv webserver/''
# '. webserver/bin/activate'
# 'pip3 install Flask'
# on flask website, go to quickstart to get start of code
# in terminal, 'set FLASK_APP=server' ## DEBUG ## export FLASK_ENV=development
# 'flask run' or 'python -m flask' # to make public 'flask run --host=0.0.0.0'
# view in web browser at http://127.0.0.1:5000/


from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def htmlpage(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save to database.'
	else:
		return 'Please don\'t panic, but something went terribly wrong!'
    


# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route("/favicon.ico")
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')