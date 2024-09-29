import requests
import pytest
from Lesson8.URL import base_url

def test_auth(self, user = 'flora', password = 'nature-fairy'):
    creds = {
        'username' : user,
        'password' : password
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.status_code == 201
    return resp.json()['userToken'] 

def get_token(self, user = 'flora', password = 'nature-fairy'):
        creds = {
           'username': user,
           'password': password
           }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken'] 

def create_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
            }
        my_headers = {}
        my_headers["x-client-token"] = get_token()
        resp = requests.post(base_url + '/employee', json=employee, headers=my_headers)
        assert resp.status_code == 201
        return resp.json()