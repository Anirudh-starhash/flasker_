from flask import Flask
app=Flask(__name__)

app.route("/")
def start():
    return '<h1>Guess a number between 0 and 9</hi>\
            <div style="width:480px">\
                <iframe allow="fullscreen" frameBorder="0" height="270"\
                    src="https://giphy.com/embed/4pqm16XH2rQopZrdFU/video"\
                        width="480">\
                </iframe>\
            </div>'

if __name__=="__main__":
    app.run(debug=True)