from pydantic import BaseModel
from jwtdown_fastapi.authentication import Token


class Account(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str


class AccountsIn(Account):
    password: str


class AccountsOut(Account):
    id: int
    modified: str
    hashed_password: str


class AccountToken(Token):
    account: AccountsOut


class Error(BaseModel):
    message: str


class AuthenticationException(Exception):
    pass


class AccountPUT(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str
    password: str


class AccountOutPUT(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str
    hashed_password: str
