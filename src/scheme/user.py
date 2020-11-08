"""
    Module with user validation models
"""

from pydantic import BaseModel, validator


class RegisterUserSchema(BaseModel):
    username: str
    password: str
    email: str

    @validator("password")
    def password_len(cls, value):
        if len(value) <= 8:
            raise ValueError('password must be longer than 8')
        return value


class AuthUserSchema(BaseModel):
    username: str
    password: str

    @validator("password")
    def password_len(cls, value):
        if len(value) <= 8:
            raise ValueError('password must be longer than 8')
        return value