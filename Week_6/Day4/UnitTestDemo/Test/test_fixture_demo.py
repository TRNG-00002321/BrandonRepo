import pytest


@pytest.fixture
def database_connection():
    # setup: establish a database connection
    print("Establishing database connection...")
    connection = "simulated_db_connection" # replace with actual connection logic
    yield connection # yield the connection to the test
    #teardown: close the database connection
    print("Closing database connection...")
    #connection.close() # replace with actual

def test_database_operation(database_connection):
    print(f"Using database connection: {database_connection}")
    assert database_connection == "simulated_db_connection"



def test_conftest_user(sample_data):
    assert sample_data["name"] == "brandon"
    assert sample_data["age"] == 28