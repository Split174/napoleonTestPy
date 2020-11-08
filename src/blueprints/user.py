from sanic.response import json
from sanic import Blueprint
from pydantic import ValidationError
from scheme.user import RegisterUserSchema
from services.user import (
    UserService,
    UserExistExcept,
    UserNotFound)
from services.offer import OfferService
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
        print(new_user.as_dict())
        return json({"user_id": new_user.id}, 201)
    except UserExistExcept:
        return json({"answer": "User with this mail or username exists"},
                    400)


@bp.route('/user/<user_id>/', methods=["GET"])
async def get_user_information(request, user_id: int):
    user_service = UserService()
    offer_service = OfferService()
    try:
        user = user_service.get_user_by_id(user_id)
    except UserNotFound as e:
        return json({"answer": "user with this id does not exist"}, 400)
    offers = offer_service.get_offers_by_user_id(user_id)
    return json({**(user.as_dict()),
                 "offers": offers}, 200)

