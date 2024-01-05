from flask import Flask, render_template
# from flask import request
app = Flask(__name__)

navigation=[{"href":"/", "caption":"Index"}, {"href":"/hello/", "caption":"Hello!"}]
footer=[
        {"title":"Index", "lists":[{"href":"/", "caption":"Index"}, {"href":"/hello/", "caption":"Hello!"}]}
        ]


@app.route('/')
def hello_world():
    global navigation
    return render_template('index.html', navigation=navigation, footer=footer)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    global navigation
    return render_template('hello.html', navigation=navigation, footer=footer, name=name)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')