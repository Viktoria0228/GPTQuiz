from .settings import project
import home_app, user_app, admin_app, library_app, execution_app, history_app, reports_app, search_app, host_app

home_app.home_app.add_url_rule(
    rule= '/',
    view_func= home_app.render_home_page
)
project.register_blueprint(blueprint= home_app.home_app)
# 
user_app.user_app.add_url_rule(
    rule= '/signup/',
    view_func= user_app.render_signup,
    methods= ["POST", "GET"]
)
user_app.user_app.add_url_rule(
    rule= '/login/',
    view_func= user_app.render_login,
    methods= ["POST", "GET"]
)
user_app.user_app.add_url_rule(
    rule= '/logout/',
    view_func= user_app.logout
)
user_app.user_app.add_url_rule(
    rule = '/profile/',
    view_func = user_app.render_profile
)

project.register_blueprint(blueprint= user_app.user_app)
admin_app.admin_app.add_url_rule(
    rule= '/admin/',
    view_func= admin_app.render_admin_page,
    methods= ["POST", "GET"]
)
project.register_blueprint(blueprint= admin_app.admin_app)

library_app.library_app.add_url_rule(
    rule= '/library/',
    view_func= library_app.render_library,
    methods= ['POST', 'GET']
)

library_app.library_app.add_url_rule(
    rule= '/create-quiz/',
    view_func= library_app.render_create_quiz,
    methods= ["POST", "GET"]
)

library_app.library_app.add_url_rule(
    rule= '/enter-answer/',
    view_func= library_app.render_enter_answer,
    methods= ["POST", "GET"]
)


project.register_blueprint(blueprint= library_app.library_app)

execution_app.execution_app.add_url_rule(
    rule = '/execution/',
    view_func = execution_app.render_execution_page,
    methods = ["POST", "GET"]
)

execution_app.execution_app.add_url_rule(
    rule = '/execution/<enter_code>/',
    view_func = execution_app.render_enter_code,
    methods = ["POST","GET"]
)
project.register_blueprint(blueprint = execution_app.execution_app)

history_app.history_app.add_url_rule(
    rule = '/history/',
    view_func= history_app.render_history,
    methods = ["POST", "GET"]
)
project.register_blueprint(blueprint = history_app.history_app)

reports_app.reports_app.add_url_rule(
    rule= '/reports/',
    view_func= reports_app.render_reports_page
)
project.register_blueprint(blueprint= reports_app.reports_app)

search_app.search_app.add_url_rule(
    rule = "/search/",
    view_func = search_app.render_search,
)
project.register_blueprint(blueprint=search_app.search_app)

host_app.host_app.add_url_rule(
    rule = '/host/<int:quizid>',
    view_func = host_app.render_host_app
)
project.register_blueprint(blueprint = host_app.host_app) 