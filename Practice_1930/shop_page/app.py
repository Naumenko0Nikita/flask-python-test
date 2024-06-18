import flask

shop_app = flask.Blueprint(
    name = "shop",
    import_name = "shop_page",
    static_folder = "static/shop",
    static_url_path = "/shop_page",
    template_folder = "templates"
)