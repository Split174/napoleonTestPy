from database import scoped_session
from scheme.user import RegisterUserSchema, AuthUserSchema
from models import UserModel
from sqlalchemy import or_
from exception import ServiceError
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
from services.offer import OfferService


class UserExistExcept(ServiceError):
    pass


class UserNotFound(ServiceError):
    pass


class UserService:
    def __init__(self):
        self.service_offer = OfferService()

    def create_user(self, user: RegisterUserSchema) -> Optional[UserModel]:
        if self._is_user_exist(user):
            raise UserExistExcept()
        password_hash = generate_password_hash(user.password)
        with scoped_session() as session:
            new_user = UserModel(username=user.username,
                                 password=password_hash,
                                 email=user.email)
            session.add(new_user)
            session.flush()
        return new_user

    def _is_user_exist(self, user: RegisterUserSchema) -> bool:
        with scoped_session() as session:
            find_user = session.query(UserModel).filter(
                or_(UserModel.email == user.email,
                    UserModel.username == user.username))\
                .first()
        return False if find_user is None else True

    def get_user_and_offers(self, user_id):
        user = self._get_user_by_id(user_id)
        offers = self.service_offer.get_offers_by_user_id(user_id)
        return user, offers

    def get_user_by_id(self, id: int) -> UserModel:
        with scoped_session() as session:
            user = session.query(UserModel).filter(UserModel.id == id).first()
            if user is None:
                raise UserNotFound()
            return user

