import flask 

def render_reports_page():
    return flask.render_template(
        template_name_or_list= 'reports.html'
    )