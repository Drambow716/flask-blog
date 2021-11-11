from flask import Blueprint,render_template,url_for,redirect,request

from src.db.db import db

from src.db.models.blog import Blogs

from slugify import slugify

import uuid

home_blueprint = Blueprint('home_blueprint', __name__,template_folder='../../templates')


@home_blueprint.route('/')
def home_route():
    q = request.args.get("q")
    cursor = db.engine.execute("SELECT DISTINCT category FROM blogs;")
    categories = [row[0] for row in cursor]
    blogs = [blog.to_dict() for blog in Blogs.query.all()]
    if q:
        blogs =  [blog.to_dict() for blog in Blogs.query.filter(Blogs.category.contains(q) | Blogs.title.contains(q) | Blogs.content.contains(q))]
        if(len(blogs)==1):
            return redirect(url_for("home_blueprint.blog_details_route",slug=blogs[0]["slug"]))
    return render_template("home.html",blogs=blogs,categories_array=categories)



@home_blueprint.route("/blog/<string:slug>")
def blog_details_route(slug):
    ## get article by sluf if its found render
    blog = Blogs.query.filter_by(slug=slug).first()
    if blog:
        return render_template("details.html",blog=blog)
    return redirect(url_for("home_blueprint.home_route"))
