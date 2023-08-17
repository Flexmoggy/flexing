from fastapi import APIRouter, Depends, HTTPException, status, Request
from models.accounts import (
    Account,
    AccountsIn,
    AccountsOut,
    AccountOutPUT,
    AccountPUT,
)
from queries.accounts import (
    AccountsRepository,
    AccountToken,
    Error,
    AuthenticationException,
)
from typing import List, Union
from authenticator import MyAuthenticator
import os

authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
router = APIRouter()


@router.post("/api/accounts")
def create_account(
    info: AccountsIn,
    accounts: AccountsRepository = Depends(),
) -> AccountsOut:
    hashed_password = authenticator.hash_password(info.password)
    ar = Account(
        user_name=info.user_name,
        first_name=info.first_name,
        last_name=info.last_name,
        email=info.email,
    )
    try:
        pk = accounts.create(ar, hashed_password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return accounts.get_account_by_id(pk)


@router.get("/api/accounts", response_model=Union[Error, List[Account]])
def list_accounts(
    repo: AccountsRepository = Depends(),
):
    return repo.get_all()


@router.get("/api/accounts/{pk}", response_model=AccountsOut)
async def get_account_details(
    pk: int,
    accounts: AccountsRepository = Depends(),
    ra=Depends(authenticator.get_current_account_data),
) -> AccountsOut:
    try:
        account = accounts.get_account_by_id(pk)
    except AuthenticationException:
        return HTTPException(status.HTTP_401_UNAUTHORIZED)
    return account


@router.put("/api/accounts/{id}", response_model=Union[AccountOutPUT, Error])
def update_account(
    id: int, accounts: AccountPUT, repo: AccountsRepository = Depends()
) -> Union[AccountOutPUT, Error]:
    hashed_password = authenticator.hash_password(accounts.password)
    return repo.update(id, accounts, hashed_password)


@router.delete("/api/accounts/{pk}", response_model=bool)
def delete_account(
    pk: int,
    repo: AccountsRepository = Depends(),
) -> bool:
    return repo.delete(pk)


@router.get("/token")
async def get_by_cookie(
    request: Request,
    account_data: dict
    | None = Depends(authenticator.try_get_current_account_data),
    accounts: AccountsRepository = Depends(),
    ra=Depends(authenticator.get_current_account_data),
) -> AccountToken:
    account = await get_account_details(
        account_data["id"], accounts=accounts, ra=ra
    )
    return {
        "access_token": request.cookies[authenticator.cookie_name],
        "type": "Bearer",
        "account": account,
    }
