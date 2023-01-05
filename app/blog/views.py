from flask import Blueprint, Flask

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route("/hello")
def hello_world():
    return "<p>Hello,World!</p>"

# it's a flask project.And for ,it's the first time to use a flask frame to build a project.
# It's a personal blog project,in some words,it's a simple one,but new to me.