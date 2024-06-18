from .settings import project_app

from home_page import show_home, home_app

from shop_page import show_shop, shop_app

home_app.add_url_rule(
    rule = "/",
    view_func = show_home,
    methods = ["GET", "POST"]
)
project_app.register_blueprint(blueprint = home_app)


shop_app.add_url_rule(
    rule = "/shop",
    view_func = show_shop,
    methods = ["GET", "POST"]
)
project_app.register_blueprint(blueprint = shop_app)