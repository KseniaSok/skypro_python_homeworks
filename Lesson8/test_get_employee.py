import requests

def test_employee():
    resp = requests.get('https://x-clients-be.onrender.com/company/')
    respone_body = resp.json

    assert resp.status_code == 200

def test_auth():
    creds = {
        'username' : 'flora',
        'password' : 'nature-fairy'
    }
    resp = requests.post('https://x-clients-be.onrender.com/auth/login', json=creds)
    
    assert resp.status_code == 201