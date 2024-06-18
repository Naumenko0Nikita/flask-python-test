import flask 
from .models import Product
from project.settings import DATABASE
import os

def show_shop():
    
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        product = Product(
            name = name
        )
        new_image = flask.request.files["image"]
        new_image.save(os.path.abspath(__file__ + f"/../static/shop/images/{name}.png"))
        DATABASE.session.add(product)
        DATABASE.session.commit()
    
    return flask.render_template(template_name_or_list = "shop.html", products = Product.query.all())