# import flask 

from flask import Flask,render_template,request
from flask_ckeditor import CKEditor

# create the application object

app = Flask(__name__)
ckeditor = CKEditor()
ckeditor.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    print(q)
    return render_template("home.html")


@app.route("/blog/<string:slug>")
def blog_details(slug):
    ## get article by sluf if its found render
    return render_template("home.html",slug=slug)


@app.route("/admin")
def admin():
    ## get article by sluf if its found render
    return render_template("admin.html")



## get to get data

## post is for sending data and creating something  usually

## put is updating 

## delete 

@app.route("/admin/new",methods=["GET","POST"])
def add_new_blog():
    if request.method=="GET":
        ## get article by sluf if its found render
        return render_template("new.html")
    else:
        data = request.form.get("ckeditor")
        title = request.form.get("title")
        category = request.form.get("category")
        print(data)
        ## get article by sluf if its found render
        return render_template("new.html")


if __name__ == "__main__":
    app.run(debug=True)