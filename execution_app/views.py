import flask 

def render_execution_page():
    return flask.render_template(
        template_name_or_list= 'enter_code.html'
    )