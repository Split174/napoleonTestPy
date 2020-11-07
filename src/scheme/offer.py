from pydantic import BaseModel, validators, root_validator
from typing import List, Optional


class CreateOfferSchema(BaseModel):
    user_id: int
    title: str
    text: str


class FindOfferSchema(BaseModel):
    offer_id: Optional[int]
    user_id: Optional[int]

    @root_validator
    def title(cls, values):
        offer_id, user_id = values.get("offer_id"), values.get("user_id")
        # если оба параметра пустые то исключение
        if not ((offer_id is not None) or (user_id is not None)):
            raise ValueError('at least one field must be filled')
        return values

