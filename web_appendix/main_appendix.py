from flask import Flask, render_template
from fastapi import Fast
from jinja2 import Template
import sys
import dearpygui as dpi
from dearpygui import *

#Run server 
# from SCZ import SCZ_client_beta

# Inport config
# import .config as configuration


title = {
    'title': 'Alpha version'
    }

#flask Run app

class main_run:
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    @app.route('/')
    def index():
            return render_template('index.html', title = title['title'])
    
    @app.route('/alp')
    def message():
        return render_template('message.html', title = title['title'])
    
    @app.route('/test')
    def test():
        return render_template('test.html', title = title['title'])

    

if __name__ == '__main__':
    application = main_run()
    application.app.run(debug=True)
    

