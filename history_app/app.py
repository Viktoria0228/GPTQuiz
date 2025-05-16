import flask

history_app = flask.Blueprint(
    name= 'history_app',
    import_name= 'history_app',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/history/'
)