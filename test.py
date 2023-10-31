from app import app
import json

def test_put_birthday_from_past():
    client = app.test_client()
    
    #Define the PUT request data
    data = {
        "dateOfBirht": "1990-05-15"
    }

    #Send the PUT request
    response = client.put('/hello/johntest', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 204

def test_put_birthday_from_future():
    client = app.test_client()

    data = {
        "dateOfBirth": "2300-10-14"
    }

    response = client.put('/hello/johntest', data=json.dumps(data), content_type='applicaiton/json')
    assert response.status_code == 400

def test_put_birthday_bad_date():
    client = app.test_client()

    data = {
        "dateOfBirht": "xyz"
    }
    response = client.put('/hello/johntest', data=json.dumps(data), content_type='applicaiton/json')
    assert response.status_code == 400

def test_put_birthday_bad_year():
    client = app.test_client()

    data = {
        "dateOfBirht": "190-44-99"
    }
    response = client.put('/hello/johntest', data=json.dumps(data), content_type='applicaiton/json')
    assert response.status_code == 400    
    
def test_put_name_with_numbers():
    client = app.test_client()
    
    data = {
        "dateOfBirt": "1982-11-05"
    }

    response = client.put('/hello/johntest123', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    