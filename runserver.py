"""
This script runs the CloudSite application using a development server.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import environ
import http.server
import socketserver
import dns.resolver
import socket
import os
from flask import send_file
import requests
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from datetime import datetime
from flask import render_template
from flask import Flask, request, abort, jsonify, send_from_directory
from flask import Flask, request, render_template, redirect, abort, url_for
from flask_cloudy import Storage
import libcloud.security
app = Flask(__name__)
libcloud.security.VERIFY_SSL_CERT = False
app.config['MAX_CONTENT_LENGTH'] = 50500 * 1024 * 1024
# Destino del archivo subido (app.config['UPLOAD_FOLDER'] = './uploads')
app.config['UPLOAD_FOLDER'] = './data'
app.config.update({
    "STORAGE_PROVIDER": "LOCAL",
    "STORAGE_CONTAINER": "./data",
    "STORAGE_KEY": "",
    "STORAGE_SECRET": "",
    "STORAGE_SERVER": True
})

storage = Storage()
storage.init_app(app)



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )



@app.route('/CloudST')
def CloudST():
    """Renders the contact page."""
    return render_template("CloudST.html", storage=storage) 

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route("/view/<path:object_name>")
def view(object_name):
    obj = storage.get(object_name)
    print (obj.name)
    return render_template("view.html", obj=obj)

@app.route("/upload", methods= ['GET','POST'])
def upload():
    if request.method =='POST':
        file = request.files.get("file")
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return render_template('CloudST.html', storage=storage)
   





if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.104", port=80)