from .settings import project
import home_app, user_app, admin_app, library_app

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
project.register_blueprint(blueprint= library_app.library_app)