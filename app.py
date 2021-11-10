# import flask 

from dotenv import load_dotenv
from os import environ
from flask import Flask,render_template,request,redirect,url_for
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from slugify import slugify
import uuid
# create the application object

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(app)
ckeditor = CKEditor()
ckeditor.init_app(app)


class Blogs(db.Model):
    id = db.Column(db.String, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String,nullable=False)
    category = db.Column(db.String,nullable=False)
    cover_url = db.Column(db.String,nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "content": self.content,
            "category": self.category,
            "cover_url": self.cover_url
        }
 



 

@app.route("/")
def home():
    q = request.args.get("q")
    cursor = db.engine.execute("SELECT DISTINCT category FROM blogs;")
    categories = [row[0] for row in cursor]
    blogs = [blog.to_dict() for blog in Blogs.query.all()]
    if q:
        blogs =  [blog.to_dict() for blog in Blogs.query.filter(Blogs.category.contains(q) | Blogs.title.contains(q) | Blogs.content.contains(q))]
        if(len(blogs)==1):
            return redirect(url_for("blog_details",slug=blogs[0]["slug"]))
    return render_template("home.html",blogs=blogs,categories_array=categories)

@app.route("/blog/<string:slug>")
def blog_details(slug):
    ## get article by sluf if its found render
    blog = Blogs.query.filter_by(slug=slug).first()
    if blog:
        return render_template("details.html",blog=blog)
    return redirect(url_for("home"))


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
        content = request.form.get("ckeditor")
        title = request.form.get("title")
        category = request.form.get("category")
        cover_url = request.form.get("cover_url")
        new_blog = Blogs(id=str(uuid.uuid4()),title=title,category=category,cover_url=cover_url,slug=slugify(title),content=content)
        db.session.add(new_blog)
        db.session.commit()
        print(new_blog)
        ## get article by sluf if its found render
        return  redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)