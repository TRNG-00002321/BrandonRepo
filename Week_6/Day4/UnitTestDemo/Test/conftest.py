import pytest

@pytest.fixture(scope="module")
def sample_data():
    data={"name":"brandon","age":28}
    yield data
    #do some thing