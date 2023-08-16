from queries.pool import pool
from typing import List, Union
from models.accounts import (
    Account,
    AccountsIn,
    AccountsOut,
    Error,
    AuthenticationException,
    AccountOutPUT,
    AccountPUT,
    AccountToken,
)


class AccountsRepository:
    def get_all(self) -> Union[Error, List[Account]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id,
                            first_name,
                            last_name,
                            email,
                            user_name
                        FROM accounts;
                        """
                    )
                    result = []
                    for record in db:
                        account = Account(
                            id=record[0],
                            first_name=record[1],
                            last_name=record[2],
                            email=record[3],
                            user_name=record[4],
                        )
                        result.append(account)

                    return result
        except Exception as e:
            return {"message": e}

    def create(self, accounts: Account, hashed_password: str) -> int:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts (
                        user_name,
                        email,
                        first_name,
                        last_name,
                        password
                        )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING ID;
                    """,
                    (
                        accounts.user_name,
                        accounts.email,
                        accounts.first_name,
                        accounts.last_name,
                        hashed_password,
                    ),
                )
                pk = result.fetchone()[0]
                return pk

    def delete(self, pk: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s
                        RETURNING *;
                        """,
                        (pk),
                    )
                    return True
        except Exception as e:
            return {False: e}

    def get_account_by_id(self, pk: int) -> AccountsOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, user_name, first_name, last_name,
                        email, password, modified
                    FROM accounts
                    WHERE id = %s;
                    """,
                    [pk],
                )
                ac = cur.fetchone()
                if ac is None:
                    raise AuthenticationException("No account found")
                else:
                    try:
                        return self.record_to_account_out(ac)
                    except Exception as e:
                        raise Exception("Error:", e)

    def get_account(self, user_name: str) -> AccountsOut | None:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id,
                            user_name,
                            first_name,
                            last_name,
                            email,
                            password,
                            modified
                          FROM accounts
                          WHERE user_name = %s;
                        """,
                        [user_name],
                    )
                    record = result.fetchone()
                    if record is None:
                        raise Exception("No account found")
                    else:
                        try:
                            return self.record_to_account_out(record)
                        except Exception as e:
                            raise Exception("Error:", e)
        except Exception as e:
            raise Exception("Error:", e)

    def record_to_account_out(self, record):
        return AccountsOut(
            id=record[0],
            user_name=record[1],
            first_name=record[2],
            last_name=record[3],
            email=record[4],
            hashed_password=record[5],
            modified=record[6].isoformat(),
        )

    def update(
        self,
        id: int,
        accounts: AccountPUT,
        hashed_password: str,
    ) -> Union[AccountOutPUT, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE accounts
                        SET email = %s,
                            password = %s,
                            user_name = %s,
                            first_name = %s,
                            last_name = %s
                        WHERE id = %s
                        RETURNING
                        email,
                        user_name,
                        first_name,
                        last_name;
                        """,
                        [
                            accounts.email,
                            hashed_password,
                            accounts.user_name,
                            accounts.first_name,
                            accounts.last_name,
                            id,
                        ],
                    )
                # id = result.fetchone()[0]
                # return self.account_in_to_out(id, accounts)
                return AccountOutPUT(
                    first_name=accounts.first_name,
                    last_name=accounts.last_name,
                    user_name=accounts.user_name,
                    email=accounts.email,
                    hashed_password=hashed_password,
                )
        except Exception as e:
            print(e, "-------------------------------")
            return Error(str(e))

    def account_in_to_out(self, id: int, accounts: AccountsIn):
        old_data = accounts.dict()
        return AccountsOut(id=id, **old_data)

    def doNothing(AccountToken: AccountToken):
        pass
