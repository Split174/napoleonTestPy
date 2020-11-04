from sanic.response import json
from sanic import Blueprint

from database import scoped_session, Session
from models.user import UserModel

bp = Blueprint('user')


@bp.route('/user/registry/', methods=["POST"])
async def register_user(request):
    pass


@bp.route('/user/auth/', methods=["POST"])
async def auth_user(request):
    pass


@bp.route('/user/<user_id>', methods=["GET"])
async def get_user(request, user_id):
    pass