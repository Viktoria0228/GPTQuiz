from .settings import project
import home_app, user_app, admin_app

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
project.register_blueprint(blueprint= user_app.user_app)
admin_app.admin_app.add_url_rule(
    rule= '/admin/',
    view_func= admin_app.render_admin_page,
    methods= ["POST", "GET"]
)
project.register_blueprint(blueprint= admin_app.admin_app)