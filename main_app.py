from flask import Flask, render_template, flash, redirect, url_for, request
from contents import images,videos
app = Flask(__name__)  # creating a Flask object
app.secret_key = "some secret"

images_list = images()
videos_list = videos()


# Home Page
@app.route("/")
def index():
    try:
        return render_template("main.html",videos=videos_list)
    except Exception as e:
        return render_template("500.html")

# Gallery
@app.route("/gallery/")
def gallery():
    try:
        return render_template("gallery.html", images=images_list, videos=videos_list)
    except Exception as e:
        return render_template("500.html")

# Login Page
@app.route("/login/", methods=['GET','POST'])
def login():
    error = None
    try:
        if request.method == "POST":
            attempted_email = request.form["email"]
            attempted_password = request.form["password"]

            if attempted_email == "anuragregmi@protonmail.com" and attempted_password == "password":
                return redirect(url_for('gallery'))
            else:
                error = "Invalid Credentials"
                flash(error)

        return render_template("login.html")
    except Exception as e:
        flash(e)
        return render_template("login.html")

# 404 error
@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run()
