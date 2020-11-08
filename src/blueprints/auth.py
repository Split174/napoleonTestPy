from sanic.response import json
from sanic import Blueprint
from pydantic import ValidationError
from scheme.user import AuthUserSchema
from services.auth import (
    AuthService,
    IncorrectlyLoginPassExcept)

bp = Blueprint('auth')


@bp.route('/user/auth/', methods=["POST"])
async def auth_user(request):
    try:
        user_data = AuthUserSchema.parse_obj(request.json)
    except ValidationError as e:
        return json((e.errors(), 400))
    service = AuthService()
    try:
        user_id, token = service.authenticate(user_data)
        return json({"user_id": user_id, "token": token},
                    200)
    except IncorrectlyLoginPassExcept:
        return json({"answer": "Password or username incorrectly"}, 400)

