from flask import Flask,render_template,url_for, request
#from rec_music import *


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def music():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        x = []
        username = request.form['username']
        try:
            for i in users[username]:
                x.append(i)
            y = recommend(username , users)
            return render_template('musicprofile.html',myband=x , recmusic = y)
        except:
            return "<h3> Sorry! something went wrong! </h3>"
    else:
        return "<h3> Bad request </h3>"

		
