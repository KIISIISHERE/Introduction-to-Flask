#import flask
from flask import Flask,render_template,request
from datetime import date
#create a flask app
app=Flask(__name__)
#display the html content when the page loads
@app. route('/',methods=['GET','POST'])
def index():
    #initiliaze a blank age
    age=""
    if request.method=='POST':
        birth_year=int(request.form['year'])
        #calculate age
        age=date.today().year-birth_year
    return render_template('index.html',age=age)
#run the app
if __name__=='__main__':
    app.run(debug=True)