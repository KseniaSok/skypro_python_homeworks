import requests
import pytest
from Lesson8.URL import base_url

def get_token(username='flora', password='nature-fairy'):
    log_password = {'username' : username, 'password' : password}
    resp_token = requests.post(base_url + '/auth/login', json=log_password)
    token = resp_token.json()['userToken']
    return token