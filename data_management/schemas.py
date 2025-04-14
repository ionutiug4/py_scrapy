from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email_address: str
    last_name: str
    first_name: str
    phone_number: str
    password: str

class OderCreate(BaseModel):
    product: str
    description: str
    services: str