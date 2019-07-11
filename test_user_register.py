import pytest
import requests
import json

def test_userLogin(supply_url):
    url = supply_url + "/register"
    data = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['id'] == 4, resp.text
    assert j['token'] == "QpwL5tke4Pnpja7X4", resp.text

def test_userLogin_noEmail(supply_url):
    url = supply_url + "/register"
    data = {
                'password': 'pistol'
           }
    response = requests.post(url, data=data)
    j = json.loads(response.text)
    assert response.status_code == 400, response.text
    assert j['error'] == "Missing email or username", response.text


def test_userLogin_noPassword(supply_url):
    url = supply_url + "/register"
    data = {
                'email': 'sydney@fife'
           }
    response = requests.post(url, data=data)
    j = json.loads(response.text)
    assert response.status_code == 400, response.text
    assert j['error'] == "Missing password", response.text