from database import scoped_session
from scheme.user import RegisterUserSchema, AuthUserSchema
from models.user import UserModel
from sqlalchemy import or_
from exception import ServiceError
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional


class UserExistExcept(ServiceError):
    pass


class IncorrectlyLoginPassExcept(ServiceError):
    pass


class UserService:
    def __init__(self):
        pass

    def create_user(self, user: RegisterUserSchema) -> Optional[UserModel]:
        if self._is_user_exist(user):
            raise UserExistExcept()
        password_hash = generate_password_hash(user.password)
        with scoped_session() as session:
            new_user = UserModel(username=user.username,
                                 password=password_hash,
                                 email=user.email)
            session.add(new_user)
        return new_user

    def _is_user_exist(self, user: RegisterUserSchema) -> bool:
        with scoped_session() as session:
            find_user = session.query(UserModel).filter(
                or_(UserModel.email == user.email,
                    UserModel.username == user.username))\
                .first()
        return False if find_user is None else True

    def auth_user(self, user: AuthUserSchema) -> Optional[UserModel]:
        with scoped_session() as session:
            user_data = session.query(UserModel).filter(UserModel.username == user.username).first()

            if user_data is None or not check_password_hash(user_data.password, user.password):
                raise IncorrectlyLoginPassExcept()
        return user_data

