from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route("/")
def nivi():
    return render_template('index.html')  

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route("/submit_form", methods = ['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write(data)
		writecsv(data)
		return redirect('/thankyou.html')
	else:
		print('Unsuccessfull')

def write(info):
	with open('database.text', mode='a') as database:
		name=info["name"]
		email=info["email"]
		text=info["text"]
		file=database.write(f'\n Name:{email},\n Email:{email},\n Text:{text}')

def writecsv(info):
	with open('database.csv',newline='', mode='a') as database:
		csv_writer=csv.writer(database, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		name=info['name']
		email=info['email']
		text=info['text']
		file=csv_writer.writerow([name,email,text])



#@app.route("/components.html")
#def components():
#	return render_template('components.html')


