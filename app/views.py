from flask import render_template, request, redirect, url_for
from app import app, queue
from time import sleep

@app.route('/', methods = ['POST','GET'])


def index():
	global queue
	if(request.method == 'POST'):
		if (request.form['submit'] == 'Up'):
			#call func to make robot go up
			print("Moving robot up")
			queue.append("Up")
		elif (request.form['submit'] == 'Down'):
			#call func to make robot go down
			print("Moving robot down")
			queue.append("Down")
		elif (request.form['submit'] == 'Left'):
			#call func to make robot go left
			print("Moving robot left")
			queue.append("Left")
		elif (request.form['submit'] == 'Right'):
			#call func to make robot go right
			print("Moving robot right")
			queue.append("Right")
		elif (request.form['submit'] == 'Rotate CW'):
			#call func to rotate robot CW
			print("Rotating robot clockwise")
			queue.append("CW")
		elif (request.form['submit'] == 'Rotate CCW'):
			#call func to rotate robot CCW
			print("Rotating robot counterclockwise")
			queue.append("CCW")
		elif (request.form['submit'] == "Execute"):
			print("Execute actions in queue")
			queue = []
	return render_template('untitled.html',title = 'Pi Controller',name = 'World', actionQueue = str(queue))
