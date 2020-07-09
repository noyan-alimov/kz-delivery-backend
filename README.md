# KZ Delivery BackEnd App

This app aims to help people and organizations to deliver items. Clients can create orders specifying which item to deliver,
pick that item from what address, deliver to where and how much would a client pay for that order.
It might be somewhat like Uber, just instead of taxi drivers, there are drivers who pick up items and deliver them.
The motivation behind this project is to help people and businesses where delivery services are not developed in their home cities.

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
In order to run the tests:
- Drop test database
- Create test database
- Run the tests
You can do so by running the following commands:
```
dropdb kzdelivery_test
createdb kzdelivery_test
python test_app.py
```
The first time you run the tests, omit the dropdb command.
Please note there are client and courier tokens that will expire. These are only for Udacity submission.

## Sign Up

To sign up and get the tokens follow [this](https://kz-delivery.eu.auth0.com/authorize?audience=kzdelivery&response_type=token&client_id=GAUVxY9vhmPm9hvlZYnyNYq2AyiVwUgO&redirect_uri=http://localhost:3000/
) link.
Sign Up and the token will be in the url as a query parameter.

Or it's better to use the below tokens that already have specific permissions:
- Client: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJ4OVU2Ty0tVk1QN3NtR3lUY2wtRSJ9.eyJpc3MiOiJodHRwczovL2t6LWRlbGl2ZXJ5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTU3NTE4MDE2OTUyNDg0Njk3OSIsImF1ZCI6WyJremRlbGl2ZXJ5IiwiaHR0cHM6Ly9rei1kZWxpdmVyeS5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0MzE2OTYwLCJleHAiOjE1OTQzODg5NjAsImF6cCI6IkdBVVZ4WTl2aG1QbTlodmxaWW55TllxMkF5aVZ3VWdPIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpvcmRlciIsImdldDpvcmRlcnNjbGllbnQiXX0.KZEPPYSQJxaW3W04n3GwHwRDpw0WEJ9hMXCEPVlT5SzqirOAwjMZnkv_24E3O6g-2ifTbPMfuyRuDSQ6Xr-DfQGaAf7Q9mqk37Xu_4Jr_v3YzU8GxLcN_zUkOmS8p9OmNI-_EToiacdgiIjwB9K5CMYkPy0ed5A40IVj3VwtVNzphGqQDNnYLHRzzk2dW5RUwmHqN7l2x4efejXwu8Ul6AMSTnkHMFtWLnts_TryEVghTvD1djnyqQ0a1UEdODZz0nqj7okLbJO7mG9CJz9GVCeXYp3BL1DY9M44pJt-4_ZdOHrHr6Cwptwk1u8kwREduXYLhGVfsEmuIgZh1Dz86A`
- Courier: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJ4OVU2Ty0tVk1QN3NtR3lUY2wtRSJ9.eyJpc3MiOiJodHRwczovL2t6LWRlbGl2ZXJ5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzg3MzY5MjkyODU5ODk4MjIzOSIsImF1ZCI6WyJremRlbGl2ZXJ5IiwiaHR0cHM6Ly9rei1kZWxpdmVyeS5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0MzE3MDM0LCJleHAiOjE1OTQzODkwMzQsImF6cCI6IkdBVVZ4WTl2aG1QbTlodmxaWW55TllxMkF5aVZ3VWdPIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjb3VyaWVyIiwiZ2V0Om9yZGVyc2NvdXJpZXIiLCJ1cGRhdGU6b3JkZXIiXX0.qbarM676kcJIA0JAqys0JbZk4-8URcpXiB7C9r8UFY9M1s3zyvEO9mcc3c0Xnrnn3kiod3fUbN8-bPZ9B6WBFbLR42TL28w2GzfFk8VXZ10bkjaGXelxFqbk93jqYcT87v159F75LHtU0W8XyIzNDA0SHPL-BdQcb0COkuJOMDJ0RKWqDzNQ7jc59cXYB2Ulpz6yrxwfIDJpMRC63hluEatSRq7TEJivlgY5RxzMGp8A1eISrJg9oq-BJLOAadOWoixIBGF2UuEMtaHpBktnWKIRziXI_NAa71iu1DWxXoHkzqF36w3cEpo0Ulb161-y99hLzsc6WTPZtzlglCdORQ`

## API Reference

### Getting started
- Base URL: [https://kz-delivery-backend.herokuapp.com/](https://kz-delivery-backend.herokuapp.com/)
- Authentication: Most API endpoints require JWT tokens. You can find them above. They are only for Udacity Nanodegreee submission, then they will expire.

### Roles and Permissions
- Client: `create:order`, `get:ordersclient`
- Courier: `update:order`, `get:ordersclient`, `delete:courier`

### Error handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
The API will return these error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not Allowed

Also, there are Authorization errors:
- 401: Unauthorized
- 403: Forbidden
Example:
```
{
  "code": "invalid_header",
  "description": "Authorization header must be bearer token."
}
```

### Endpoint Library

#### GET /
General:
- Returns a success value and orders that have not been chosen by couriers.
Sample: `curl https://kz-delivery-backend.herokuapp.com/`
```
{
  "orders": [
      {
          "client_id": 1,
          "from_address": "11 str",
          "id": 3,
          "item": "flowers",
          "price": 12,
          "to_address": "54 str"
      }
  ],
  "success": true
}
```

#### POST /couriers
General:
- Takes the name as a parameter, returns success value and new ID of a courier.
Sample: `curl https://kz-delivery-backend.herokuapp.com/couriers -X POST -H "Content-Type: application/json" -d '{"name":"John"}'`
```
{
  "new_courier_id": 2,
  "success": true
}
```

#### POST /clients
General:
- Takes the name as a parameter, returns success value and new ID of a client.
Sample: `curl https://kz-delivery-backend.herokuapp.com/couriers -X POST -H "Content-Type: application/json" -d '{"name":"John"}'`
```
{
  "new_client_id": 2,
  "success": true
}
```

#### POST /orders
General:
- Takes the item, from address, to address and a price as parameters, returns success value and new order id.
- Requires permissions available from a client.
Sample: `curl https://kz-delivery-backend.herokuapp.com/orders -X POST -H "Authorization: Bearer ${CLIENT_TOKEN}" -H "Content-Type: application/json" -d '{
    "item": "flowers",
    "from_address": "11 str",
    "to_address": "54 str",
    "price": 12,
    "client_id": 1
}'`
```
{
  "new_order_id": 2,
  "success": True
}
```

#### PATCH /orders/{order_id}
General:
- Takes the courier id, returns success value, order id and courier id.
- Requires permissions available from a courier.
Sample: `curl https://kz-delivery-backend.herokuapp.com/orders/2 -X PATCH -H "Authorization: Bearer ${COURIER_TOKEN}" -H "Content-Type: application/json" -d '{
    "courier_id": 1
}'`
```
{
  "courier_id": 1,
  "order_id": 2,
  "sucess": True
}
```

#### GET /couriers/{courier_id}/orders
General:
- Returns success value and orders that were updated by specific courier.
- Requires permissions available from a courier.
Sample: `curl https://kz-delivery-backend.herokuapp.com/couriers/1/orders -H "Authorization: Bearer ${COURIER_TOKEN}"`
```
{
  "orders": [
    {
      "item": "flowers",
      "from_address": "11 str",
      "to_address": "54 str",
      "price": 12,
      "client_id": 1
    }
  ],
  "success": True
}
```

#### GET /clients/{client_id}/orders
General:
- Returns success value and orders that were created by specific client.
- Requires permissions available from a client.
Sample: `curl https://kz-delivery-backend.herokuapp.com/clients/1/orders -H "Authorization: Bearer ${CLIENT_TOKEN}"`
```
{
  "orders": [
    {
      "item": "flowers",
      "from_address": "11 str",
      "to_address": "54 str",
      "price": 12,
      "client_id": 1
    }
  ],
  "success": True
}
```

#### DELETE /couriers/{courier_id}
General:
- Deletes a courier, returns success value and deleted courier id.
- Requires permissions available from a courier.
Sample: `curl https://kz-delivery-backend.herokuapp.com/orders/2 -X DELETE -H "Authorization: Bearer ${COURIER_TOKEN}"`
```
{
  "deleted_courier_id": 1,
  "success": True
}
```

## Authors
Noyan Alimov
