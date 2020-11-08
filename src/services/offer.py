"""
    Module with offer service
"""
from database import scoped_session
from scheme.offer import CreateOfferSchema
from models import OfferModel
from typing import List, Dict


class OfferService:
    def __init__(self):
        pass

    def create_offer(self, offer: CreateOfferSchema) -> OfferModel:
        with scoped_session() as session:
            new_offer = OfferModel(user_id=offer.user_id,
                                   title=offer.title,
                                   text=offer.text)
            session.add(new_offer)
            session.flush()
        return new_offer

    def get_offers_by_user_id(self, user_id) -> List[Dict]:
        with scoped_session() as session:
            offers = session.query(OfferModel).filter(OfferModel.user_id == user_id).all()
        return [o.as_dict() for o in offers]

    def get_offer_by_id(self, offer_id) -> OfferModel:
        with scoped_session() as session:
            offer = session.query(OfferModel).filter(OfferModel.id == offer_id).first()
        return offer

