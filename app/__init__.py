from flask import Flask
app = Flask(__name__)
queue = []
from app import views