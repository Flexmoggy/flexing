from main import app
from fastapi.testclient import TestClient
from queries.accounts import AccountsRepository

client = TestClient(app)


class Empty_Accounts:
    def get_all(self):
        return []


def test_get_all_Accounts():
    # arrange
    app.dependency_overrides[AccountsRepository] = Empty_Accounts

    response = client.get("/api/accounts/")
    # act
    app.dependency_overrides = {}

    # assert
    assert response.status_code == 200
    assert response.json() == []
