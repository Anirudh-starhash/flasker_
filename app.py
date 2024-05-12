from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


# create a flask instance
app=Flask(__name__)
app.config["SECRET_KEY"]="That does'nt concern me"

# create a flask form
class nameform(FlaskForm):
    name=StringField("Whats your name",validators=[DataRequired()])
    submit=SubmitField("Submit")


@app.route("/")

# def index():
#     return '<h1>Hello</h1>'

def index():
    stuff="This is <strong>Bold</strong> Text"
    favorite_cars=['Audi','Mercedes','Ferrari','Lamborgini',41]
    return render_template("index.html",stuff=stuff,favorite_cars=favorite_cars)

@app.route("/user/<name>")

# def user(name):
#     return '<h1>Hello {} !!!</h1>'.format(name)

def user(name):
    return render_template("user.html",name=name)

# creating a custom error pages

# for invalid url
@app.errorhandler(404)

def invalid(e):
    return render_template("404.html"),404

# for internal servor issue
@app.errorhandler(500)

def internal_server(e):
    return render_template("500.html"),500

@app.route("/name",methods=['GET','POST'])

def name():
    name=None
    form=nameform()
    
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash('Form Submitted Successfully')
        
    return render_template('name.html',form=form,name=name)




if __name__=='__main__':
    app.run(debug=True)