from flask import Blueprint,render_template,url_for,redirect,request
from flask import Blueprint
from src.db.models.blog import Blogs
from src.db.db import db
from slugify import slugify
import uuid





admin_blueprint = Blueprint('admin_blueprint', __name__,template_folder='../../templates')




@admin_blueprint.route("/admin")
def admin_panel_route():
    ## get article by sluf if its found render
    return render_template("admin.html")




@admin_blueprint.route("/admin/new",methods=["GET","POST"])
def create_blog_route():
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
        ## get article by sluf if its found render
        return  redirect(url_for("home_blueprint.home_route"))

