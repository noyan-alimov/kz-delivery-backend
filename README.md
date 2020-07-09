# KZ Delivery BackEnd App

This app aims to help people and organizations to deliver items. Clients can create orders specifying which item to deliver,
pick that item from what address, deliver to where and how much would a client pay for that order.
It might be somewhat like Uber, just instead of taxi drivers, there are drivers who pick up items and deliver them.
The motivation behind this project is to help people where delivery services like DHL are not developed in their home countries or cities.

## Getting started

This [project](https://kz-delivery-backend.herokuapp.com/) is deployed via Heroku. You can test API endpoints using curl or postman. Before that, please go through the Sign Up process which is described further below.
To run the project locally follow the below instructions.

### Pre-requisites and Local Development

Python3 and pip should already be installed.
Run `pip install requirements.txt`. This will install all the required packages.

To run the application run the following commands:
```
export FLASK_APP=app.py
export FLASK_ENV=development
python app.py
```

The application will run on `http://127.0.0.1:5000/` by default.

#### Tests
In order to run the tests replace the courier token and client token variables after sign up process which would be described later below.
Then run the following commands:
```
dropdb kzdelivery_test
createdb kzdelivery_test
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command.

## Sign Up

To sign up and get the tokens follow [this](https://kz-delivery.eu.auth0.com/authorize?audience=kzdelivery&response_type=token&client_id=GAUVxY9vhmPm9hvlZYnyNYq2AyiVwUgO&redirect_uri=http://localhost:3000/
) link.
Save the token
