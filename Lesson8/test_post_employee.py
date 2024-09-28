import requests
import pytest
from Lesson8.URL import base_url

def test_auth():
    creds = {
        'username' : 'flora',
        'password' : 'nature-fairy'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_employee():
    creds = {
        'username' : 'flora',
        'password' : 'nature-fairy'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

    employee = {
        "id": 0,
        "firstName": "Oks",
        "lastName": "Sok",
        "middleName": "Val",
        "companyId": 0,
        "email": "oksok@gmail.ru",
        "url": "none",
        "phone": "89999999999",
        "birthdate": "2024-09-28T12:21:38.971Z",
        "isActive": true
        }
    
    my_headers = {}
    my_headers["x-client-token"] = token
    resp = requests.post(base_url + '/employee', json=employee, headers=my_headers)
    assert resp.status_code == 201