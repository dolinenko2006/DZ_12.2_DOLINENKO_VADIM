from flask import Blueprint, render_template, request
from main.utils import PostHandler
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route("/")
def mein_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    subst = request.args.get('s')
    post_handler = PostHandler('post.json')
    post = post_handler.search_posts(substr)
    return render_template('post_list.html', posts=posts, subst=subst)

