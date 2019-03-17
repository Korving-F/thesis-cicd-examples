import pytest
import json
from example import static_funcs as sf
from example.app import App

@pytest.fixture()
def test_client():
    example_app = App()
    test_client = example_app.app.test_client()
    ctx = example_app.app.app_context()
    ctx.push()
    yield test_client
    ctx.pop()

def test_reversing_of_string():
    newstr = sf.string_reverser("CI Tools are swell!")
    assert newstr == "!llews era slooT IC"

def test_reversing_of_long_string_fails():
    newstr = sf.string_reverser("CI Tools are not useful at all!")
    assert newstr is None, "Long strings should fail to be reversed."

def test_five_should_be_prime():
    assert sf.is_prime(5) is True

def test_six_should_not_be_prime():
    assert sf.is_prime(6) is False

def test_200_code_on_valid_request(test_client):
    r = test_client.get('/todos')
    assert r.status_code == 200

def test_404_code_on_incorrect_request(test_client):
    r = test_client.get('/todos/doesntexist')
    assert r.status_code == 404

def test_error_message_on_incorrect_request(test_client):
    r = test_client.get('/todos/a')
    assert json.loads(r.data.decode('utf-8'))['message'] == "Todo a doesn't exist"

def test_task_description_on_get_request(test_client):
    r = test_client.get('/todos/todo1')
    assert json.loads(r.data.decode('utf-8'))['task'] == "Analyize various CI tools"

def test_task_gets_added_on_post(test_client):
    r = test_client.post("/todos?task=Test the application!")
    assert r.status_code == 201
    assert json.loads(r.data.decode('utf-8'))['task'] == "Test the application!"

def test_task_gets_deleted_on_delete(test_client):
    r = test_client.delete("/todos/todo2")
    assert r.status_code == 204
    assert r.data is b'', "Returned value should be empty byte array"
