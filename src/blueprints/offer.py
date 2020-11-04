from sanic.response import json
from sanic import Blueprint

from database import scoped_session, Session
from models.offer import OfferModel

bp = Blueprint('offer')


@bp.route('/offer/create/', methods=["POST"])
async def create_offer(request):
    pass


@bp.route('/offer/', methods=["POST"])
async def get_offer(request):
    pass
