import requests
import pytest
from Lesson8.URL import base_url

def get_employee(self, id):
    resp = requests.get(self.url + '/employee' + str(id))
    return resp.json()

def test_get_employee():
    firstName = "Oks"
    lastName = "Sok"
    middleName = "Val"
    email = "oksok@gmail.ru"
    phone = "89999999999"
    result = (firstName, lastName, middleName, email, phone)
    new_id = result["id"]
    new_employee = get_employee(new_id)
    
    assert new_employee['id'] == new_id
    
def edit(self):
        creds = {
        'username' : 'flora',
        'password' : 'nature-fairy'
        }
        resp = requests.post(base_url + '/auth/login', json=creds)
        token = resp.json()["userToken"]
       
        my_headers = {}
        my_headers["x-client-token"] = self.token()
        
        firstName = "Oks"
        lastName = "Sok"
        middleName = "Val"
        email = "oksok@gmail.ru"
        phone = "89999999999"
        result = (firstName, lastName, middleName, email, phone)
        new_id = result["id"]
        new_employee = get_employee(new_id)

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
        "isActive": True
        }
        resp = requests.patch(base_url + 'employee/' + str(new_id), 
                              headers=my_headers, json=creds)
        return resp.json()

def test_edit():
    firstName = "Oks"
    lastName = "Sok"
    middleName = "Val"
    email = "oksok@gmail.ru"
    phone = "89999999999"
    result = (firstName, lastName, middleName, email, phone)
    new_id = result["id"]

    new_firstName = "Ok"
    new_lastName = "So"
    new_middleName = "Va"
    new_email = "oksok@mail.ru"
    new_phone = "88899999999"

    edited = edit(new_id, new_firstName, new_lastName, new_middleName, new_email, new_phone)
    assert edited["id"] == new_id
    assert edited["firstName"] == new_firstName
    assert edited["lastName"] == new_lastName
    assert edited["middleName"] == new_middleName
    assert edited["email"] == new_email
    assert edited["phone"] == new_phone