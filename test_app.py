import pytest
from app import app
import json


@pytest.fixture
def client():
    return app.test_client()

def test_sample(client):
    out_put=client.get("/ping")
    assert out_put.json=={"msg":"ARUN'S FRIST FLASK TRY"}

def test_sample(client):
    input_data={"Fuel":"Diesel","Engine":1300.0,"Transmission":"Automatic","Seat":5,"yr":2019.0,"Seller":"Individual","KM":490500.00,"Mileage":25,"Power":125.00}
    resp=client.post("/predict",json=input_data)
    assert resp.status_code==200