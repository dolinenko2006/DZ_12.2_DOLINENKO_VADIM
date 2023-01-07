from flask import Blueprint, render_template, request
from loader.utils import save_picture
from main.utils import PostHandler
import logging



logger= logging.getLogger()
logger.setLevel(logging.DEBUG) # or whatever
handler = logging.FileHandler('basic.log', 'w', 'utf-8') # or whatever
formatter = logging.Formatter('%(name)s %(message)s') # or whatever
handler.setFormatter(formatter) # Pass handler as a parameter, not assign
logger.addHandler(handler)
#handler = logging.FileHandler('basic.log', 'w', encoding='utf-8')  # так не работает тоже
#logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8') # так не работает тоже
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route("/post")
def create_new_post_page():
    return render_template('post_form.html')

@loader_blueprint.route("/post", methods=['POST'])
def create_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
           return 'Не все поля заполнены'

    picture_path = save_picture(picture)
    if not picture_path:
        logging.info('Загружено не изображение')
        return 'Загружено не изображение'

    post_handler = PostHandler('posts.json')
    new_post = {'pic': picture_path, 'content': content}
    post_handler.add_post(new_post)
    return render_template('post_uploaded.html', picture_path=picture_path, content=content)



