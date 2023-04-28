from flask import Flask, render_template ,Blueprint

app = Flask(__name__)

# Pass the required route to the decorator.


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dontgohere")
def dont():
    return render_template("picture.html")

@app.route("/test")
def hello():
    return "Healthy"


if __name__ == "__main__":
    app.run(debug=True)
