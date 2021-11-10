# import flask 

from flask import Flask,render_template

# create the application object

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<string:slug>")
def blog_details(slug):
    ## get article by sluf if its found render
    return render_template("home.html",slug=slug)


if __name__ == "__main__":
    app.run(debug=True)