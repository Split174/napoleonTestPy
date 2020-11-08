"""
    Module for routing creation and search offers
"""
from sanic.response import json
from sanic import Blueprint
from pydantic import ValidationError
from services.offer import OfferService
from scheme.offer import CreateOfferSchema, FindOfferSchema
from services.user import UserService, UserNotFound
from services.auth import AuthService
bp = Blueprint('offer')


@bp.route('/offer/create/', methods=["POST"])
async def create_offer(request):
    """
    Create new offer
    из-за требования user_id в теле запроса, код вышел запутанный
    приходется проверять user_id в токене с user_id в теле запроса
    :param request:
    :return: json offer
    """
    try:
        offer_data = CreateOfferSchema.parse_obj(request.json)
    except ValidationError as e:
        return json(e.errors(), 422)

    try:
        is_current_user = AuthService().indentify(request, "user_id")
    except:
        return json({"answer": "not a valid token"}, 401)
    if not is_current_user:
        return json({"answer": "not a valid token"}, 401)
    try:
        user = UserService().get_user_by_id(offer_data.user_id)
    except UserNotFound as e:
        return json({"answer": "user with this id does not exist"}, 400)
    offer_serivce = OfferService()
    new_offer = offer_serivce.create_offer(offer_data)
    return json(new_offer.as_dict(), 201)


@bp.route('/offer/', methods=["POST"])
async def get_offer(request):
    """
    Get offer/offers by offer_id or user_id
    :param request:
    :return: List[offer] of offer
    """
    try:
        offer_data = FindOfferSchema.parse_obj(request.json)
    except ValidationError as e:
        return json(e.errors(), 422)
    service_offer = OfferService()
    if offer_data.offer_id is not None:
        offer = service_offer.get_offer_by_id(offer_data.offer_id)
        return json(offer.as_dict(), 200)
    if offer_data.user_id is not None:
        offers = service_offer.get_offers_by_user_id(offer_data.user_id)
        return json({"offers": offers}, 200)
