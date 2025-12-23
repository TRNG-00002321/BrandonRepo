import requests
import pytest



@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture()
def session():
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json"
    })

    yield session
    session.close()

@pytest.fixture(scope="module")
def sample_post():
    return{
    "title":"Test Post",
    "body": "Test Body Content",
    "user": 1
}

class TestBasicRequest:

    def test_get_single_post(self, base_url,session):
        response=session.get(f"{base_url}/posts/1")

        assert response.status_code == 200

        data = response.json()
        assert data["id"] == 1
        assert "title" in data