import requests
import pytest
from Lesson8.URL import url_hw8

def get_token(username='flora', password='nature-fairy'):
    log_password = {'username' : username, 'password' : password}
    resp_token = requests.post(url_hw8 + '/auth/login', json=log_password)
    token = resp_token.json()['UserToken']
    return token