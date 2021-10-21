from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.cache = {}
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

app.run(debug=True)
