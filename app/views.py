from flask import render_template, request
from app import app

@app.route('/', methods = ['POST','GET'])
def index():
	if(request.method == 'POST'):
		if (request.form['submit'] == 'Up'):
			#call func to make robot go up
			print("Moving robot up")
		elif (request.form['submit'] == 'Down'):
			#call func to make robot go down
			print("Moving robot down")
		elif (request.form['submit'] == 'Left'):
			#call func to make robot go left
			print("Moving robot left")
		elif (request.form['submit'] == 'Right'):
			#call func to make robot go right
			print("Moving robot right")
		elif (request.form['submit'] == 'Rotate CW'):
			#call func to rotate robot CW
			print("Rotating robot clockwise")
		elif (request.form['submit'] == 'Rotate CCW'):
			#call func to rotate robot CCW
			print("Rotating robot counterclockwise")
	return render_template('untitled.html',title = 'Pi Controller',name = 'World')