from flask import Flask,request,jsonify
import pickle
import sklearn
import numpy as np

app=Flask(__name__)

@app.route("/ping")
def sample():
    return "ARUN'S FRIST FLASK TRY"

encode_dict={
    "fuel_type":{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    "seller_type":{'Dealer':1,'Individual':2,'Trustmark Dealer':3},
    "transmission_type":{'Manual':1,'Automatic':2}
}

@app.route("/predict",methods=['post'])
def model_prediction():
    with open("car_pred_pickle",'rb') as file:
        reg_model=pickle.load(file)

    # Getting the user input via json format
    user_input=request.get_json()
    # Decoding the user input to respective features

    fuel=encode_dict["fuel_type"][user_input['Fuel']]
    transmission=encode_dict["transmission_type"][user_input['Transmission']]
    seller=encode_dict["seller_type"][user_input['Seller']]
    yr=user_input['yr']
    km_driven=user_input['KM']
    mileage=user_input['Mileage']
    engine=user_input['Engine']
    power=user_input['Power']
    seat=user_input['Seat']
    Input_feature=[[yr,seller,km_driven,fuel,transmission,mileage,engine,power,seat]]
    pred=np.round(reg_model.predict(Input_feature)[0],3)
    return {"Prediction":f"The Price of Car which your looking for is {pred} lakhs Rupees"}

#request=("Fuel":'Diesel','Engine':1300.0,'Transmission':'Automatic','Seat':5,'yr':2019.0,'Seller':'Individual','KM':490500.00,'Mileage':25,'Power':125.00}