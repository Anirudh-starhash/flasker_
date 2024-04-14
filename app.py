from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")

# def index():
#     return '<h1>Hello</h1>'

def index():
    return render_template("index.html")

@app.route("/user/<name>")

# def user(name):
#     return '<h1>Hello {} !!!</h1>'.format(name)

def user(name):
    stuff="This is <strong>Bold</strong> Text"
    favorite_cars=['Audi','Mercedes','Ferrari','Lamborgini',41]
    return render_template("user.html",name=name,stuff=stuff,favorite_cars=favorite_cars)

# creating a custom error pages

# for invalid url
@app.errorhandler(404)

def invalid(e):
    return render_template("404.html"),404

# for internal servor issue
@app.errorhandler(500)

def internal_server(e):
    return render_template("500.html"),500




if __name__=='__main__':
    app.run(debug=True)