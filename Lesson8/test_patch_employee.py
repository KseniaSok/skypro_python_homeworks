import requests
import pytest
from Lesson8.URL import base_url

def get_token(self, user = 'flora', password = 'nature-fairy'):
        creds = {
           'username': user,
           'password': password
           }
        resp = requests.post(base_url + '/auth/login', json=creds)
        return resp.json()['userToken'] 

def edit_employee(self, id, new_lastName, new_email, new_url, new_phone, new_isActive):
        employee = {
           "lastName": new_lastName,
           "email": new_email,
           "url":  new_url,
           "phone": new_phone,
           "isActive": new_isActive
           }
        my_headers = {"x-client-token": get_token()} 
        resp = requests.patch(base_url + '/employee/' + str(id), headers=my_headers, json=employee)
        return resp.json()

def delete_employee(self, id):
        employee = {
           "id": id
           }
        my_headers = {"x-client-token": get_token()} 
        resp = requests.delete(base_url + f'/employee/{id}', headers=my_headers)
        return resp.json()