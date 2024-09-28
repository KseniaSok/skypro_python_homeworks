import requests
import pytest
from Lesson8.URL import base_url

def test_employee():
    resp = requests.get(base_url + '/employee')
    respone_body = resp.json

    assert resp.status_code == 200
    assert len(respone_body) > 0

def test_auth():
    creds = {
        'username' : 'flora',
        'password' : 'nature-fairy'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_get_active_employee():
    resp = requests.get(base_url + '/employee')
    full_list = resp.json()
    resp = requests.get(base_url+'/employee?active=true')
    filtered_list = resp.json()
    
    assert len(full_list) > len(filtered_list)