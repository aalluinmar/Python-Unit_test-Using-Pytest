import pytest
import requests
import json

@pytest.mark.parametrize("userID, userEmail, first_name, last_name", [(2, "janet.weaver@reqres.in", "Janet", "Weaver")])
def test_get_Credentials(supply_url, userID, userEmail, first_name, last_name):
    url = supply_url + "/users/" + str(userID)
    response = requests.get(url)
    j = json.loads(response.text)
    assert response.status_code == 200, response.text
    assert j['data']['id'] == 2, response.text
    assert j['data']['email'] == 'janet.weaver@reqres.in', response.text
    assert j['data']['first_name'] == 'Janet', response.text
    assert j['data']['last_name'] == 'Weaver', response.text