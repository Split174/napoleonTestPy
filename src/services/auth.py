from datetime import datetime, timedelta
import jwt
from jwt import InvalidSignatureError

from config import Config
from database import scoped_session
from models import UserModel
from exception import ServiceError
from werkzeug.security import check_password_hash
from typing import Tuple
from scheme.user import AuthUserSchema


class IncorrectlyLoginPassExcept(ServiceError):
    pass


class NotExistToken(ServiceError):
    pass

class AuthService:
    @staticmethod
    def encode_auth_token(user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(seconds=60),
            'data': {
                'user_id': user_id,
            }
        }
        return jwt.encode(
            payload,
            Config.SECRET_KEY
        )

    @staticmethod
    def decode_auth_token(auth_token):
        payload = jwt.decode(auth_token, Config.SECRET_KEY, options={'verify_exp': True})
        if 'data' in payload and 'user_id' in payload['data']:
            return payload

    def authenticate(self, auth_schema: AuthUserSchema) -> Tuple[int, bytes]:
        password, username = auth_schema.password, auth_schema.username
        with scoped_session() as session:
            user = session.query(UserModel).filter(UserModel.username == username).first()
            if user is None:
                raise IncorrectlyLoginPassExcept()
            if check_password_hash(user.password, password):
                token = self.encode_auth_token(user.id)
                return user.id, token.decode()
            else:
                raise IncorrectlyLoginPassExcept()

    def indentify(self, request, field_check: str):
        if request.headers["token"] is None:
            raise NotExistToken()
        user_id = self.decode_auth_token(request.headers["token"])["data"][field_check]
        if int(request.json[field_check]) == user_id:
            return True
        return False

