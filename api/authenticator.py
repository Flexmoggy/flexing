import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountsRepository
from models.accounts import AccountsOut, Account


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        user_name: str,
        accounts: AccountsRepository,
    ) -> Account:
        # Use your repo to get the account based on the
        # username (which could be an email)
        return accounts.get_account(user_name)

    def get_account_getter(
        self,
        accounts: AccountsRepository = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: Account):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: Account):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.user_name, AccountsOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
