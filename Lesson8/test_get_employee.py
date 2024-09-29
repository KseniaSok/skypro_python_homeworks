import requests
import pytest
from Lesson8.URL import base_url

def test_employee():
    resp = requests.get(base_url + '/employee')
    respone_body = resp.json

    assert resp.status_code == 200
    assert len(respone_body) > 0
    return resp.json()

def get_employees_list(self,companyId):
    params = {'company': companyId}
    resp = requests.get(base_url + '/employee', params=params)
    return resp.json()