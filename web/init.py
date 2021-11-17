from flask import Flask,render_template
import flask
from flask import request, redirect

app = flask.Flask(__name__,template_folder='templates')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
        return flask.redirect("https://asarwedssajna.com")



@app.route('/location', methods=['GET'])
def loation():
    return flask.redirect("https://www.google.com/maps/place/Peer+Mohammed+Appa+Dargha+and+Auditorium/@8.2471189,77.3139151,1365m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3b04f8e5efa20c59:0x24d09e8c1d90d1af!8m2!3d8.2471299!4d77.316148")




app.run('0.0.0.0', debug=True, port=80)

