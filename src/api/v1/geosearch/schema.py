from pydantic import BaseModel


class FindStreetSchema(BaseModel):
    street: str
