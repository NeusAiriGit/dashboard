from flask import Flask, render_template
from flask import request
from dash_app import create_dash_application



app = Flask(__name__)



if __name__ == '__main__':
    app.run()
    create_dash_application(app)

