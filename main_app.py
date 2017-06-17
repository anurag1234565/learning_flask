from flask import Flask, render_template

app = Flask(__name__)  # creating a Flask object

@app.route("/")
def index():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host="localhost",port=8000, debug=True)
