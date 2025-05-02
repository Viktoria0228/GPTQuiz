import flask

def render_admin_page():
    return flask.render_template(
        template_name_or_list= 'admin.html'
    )