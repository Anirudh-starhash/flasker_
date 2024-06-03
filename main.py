from flask import Flask
app=Flask(__name__)


def make_bold(function):
    def wrapper_function():
       return '<b>'+function()+'</b>'
    return wrapper_function

def make_em(function):
    def wrapper_function():
        return '<em>'+function()+'</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return '<u>'+function()+'</u>'
    return wrapper_function


@app.route("/")

def start():
    return 'Hello World'

@app.route("/bye")
@make_bold
@make_em
@make_underlined
def bye():
    return 'Bye World'

@app.route("/username/<name>/<int:number>")

def greet(name,number):
    return f'<h1 style="text-align:center">Hello {name} and your id is {number}</h1>'\
            '<div style="width:480px">\
               <iframe allow="fullscreen" frameBorder="0" height="250" \
                   src="https://giphy.com/embed/cwQCUhKible5mGrtMO/video"\
                       width="480">\
                </iframe>\
            </div>'


if __name__=="__main__":
    app.run(debug=True)