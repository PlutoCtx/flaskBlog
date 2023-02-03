from flask import Blueprint, render_template

bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates', static_folder='static')


def index():
    return render_template('../templates/index.html')

# it's a flask project.And for ,it's the first time to use a flask frame to build a project.
# It's a personal blog project,in some words,it's a simple one,but new to me.