import flask

search_app = flask.Blueprint(
    name = "search_app",
    import_name = "search_app",
    static_folder = "static",
    static_url_path = "/searchapp/",
    template_folder = "templates"
)