from sanic.response import json
from sanic import Blueprint, response
from pydantic import ValidationError
from database import scoped_session, Session
from models.user import UserModel
from scheme.user import AuthUserSchema, RegisterUserSchema
from services.user import (
    UserService,
    IncorrectlyLoginPassExcept,
    UserExistExcept)
from datetime import datetime, timedelta
import jwt
from config import Config

bp = Blueprint('user')


@bp.route('/user/registry/', methods=["POST"])
async def register_user(request):
    try:
        user = RegisterUserSchema.parse_obj(request.json)
    except ValidationError as e:
        return json(e.errors(), 400)
    service = UserService()
    try:
        new_user = service.create_user(user)
        return json({"user_id": new_user.id}, 201)
    except UserExistExcept as e:
        return json({"answer": "User with this mail or username exists"},
                    400)


@bp.route('/user/auth/', methods=["POST"])
async def auth_user(request):
    try:
        user_data = AuthUserSchema.parse_obj(request.json)
    except ValidationError as e:
        return json((e.errors(), 401))
    service = UserService()
    try:
        user = service.auth_user(user_data)
        print(user.as_dict())
        token = jwt.encode({
            'public_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, Config.SECRET_KEY)
        return json({"user_id": user.id,
                     "token": token.decode('UTF-8')},
                    200)
    except IncorrectlyLoginPassExcept as e:
        return json({"answer": "Password or email incorrectly"}, 401)


@bp.route('/user/<user_id>', methods=["GET"])
async def get_user(request, user_id):
    pass