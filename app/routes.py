from app import app
from flask import render_template, request
from app.models import model, formopener

from flask import render_template
from flask import request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Edeline','fav_color':'pink'}
    weather = {'temperature':"70",'cloud':"cloudy"}
    return render_template('index.html', title='Home Page', user=user, weather = weather)

@app.route('/sendBreakfast',methods=['GET','POST'])
def handleBreakfast():
    if request.method == 'GET':
        user = {'name':'Edeline','fav_color':'pink'}
        weather = {'temperature':"70",'cloud':"cloudy"}
        return render_template('index.html', title='Home Page', user=user, weather = weather)
        
    else: ##this is for POST requests
        userdata = formopener.dict_from(request.form) #This puts form data into a dictionary
        nickname = userdata['nickname'] # the key for this dictionary comes from the name of the corresponding input in the <form> on the html
        breakfast = model.shout(userdata['breakfast'])
        return render_template('results.html',nickname = nickname, breakfast = breakfast)

# @app.route creates a route that we can get to in our url.
# The function decides (returns) what that route should lead to
# The function that returns for a route follows right after the route definition
@app.route('/secret')
def secretSauce():
    return "<h1>You found a secret</h1>"

@app.route('/food')
def food():
    return "<h1>Fav Foods</h1> <ul> <li>Pizza</li> <li>Chocolate </li> </ul>"

@app.route('/subways')
def subways():
    return "<h1>Subways by my house</h1><h2>2 Train</h2><h2>3 Train</h2><h2>4 Train</h2><h2>5 Train</h2><h2>6 Train</h2>"
    
@app.route('/degrees')
def degrees():
    return "<h1>Degrees I Have</h1><ol><li>Advanced Regents Diploma with Honors</li><li>International Baccalaureate Diploma</li><li>BA in Physics</li><li>MS in Physics</li><li>MST in Science Teaching</li></ol>"