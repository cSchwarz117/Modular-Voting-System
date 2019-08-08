from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
import socket
app.config["DEBUG"] = True
from client import pyClient
from messageInstance import instance
HOST = '127.0.0.1'  # The server's hostname of IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.connect((HOST, PORT))
#   instance(s)
#   s.setblocking(1)
#   usr = 'Anne'
#    pwd = 'netflix'
#    cred = {"username": usr, "password": pwd}
#    instance.send(cred)
#    inst = instance.rec()
#    print(inst)

@app.route('/')
@app.route('/index')
def index():
#    client = pyClient()
#    client.conn(HOST, PORT)
#    user = {'username': "Cole"}
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
 #      try:
   #         user = request.form["username"]
   #         pwrd = request.form["password"]

#    try:
 #   if form.validate_on_submit():
#        flash('Login requested for user {}' .format(form.username.data))
 #       return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():

    return render_template('welcome.html', title='Menu')
