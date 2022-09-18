from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/') # arg1 = blueprint's nickname(url name), arg2 = file name, arg3 = url prefix


@bp.route('/hello/') # mapping requested urls with under codes
def hello_pybo():
    return 'hello Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list')) # url_for finds url by its name with a reverse approach
