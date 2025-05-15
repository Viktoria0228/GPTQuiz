import flask 

def render_execution_page():
    return flask.render_template(
        template_name_or_list= 'enter_nickname.html'
    )

def render_enter_code(enter_code):
    return flask.render_template(
        template_name_or_list="enter_code.html"
    )