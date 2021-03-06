# KZ Delivery BackEnd App

This app aims to help people and organizations to deliver items. Clients can create orders specifying which item to deliver,
pick that item from what address, deliver to where and how much would a client pay for that order.
It might be somewhat like Uber, just instead of taxi drivers, there are drivers who pick up items and deliver them.
The motivation behind this project is to help people and businesses where delivery services are not developed in their home cities.

## Getting started

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
  Sample: `curl https://kz-delivery-backend.herokuapp.com/orders -X POST -H "Authorization: Bearer ${CLIENT_TOKEN}" -H "Content-Type: application/json" -d '{ "item": "flowers", "from_address": "11 str", "to_address": "54 str", "price": 12, "client_id": 1 }'`

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
  Sample: `curl https://kz-delivery-backend.herokuapp.com/orders/2 -X PATCH -H "Authorization: Bearer ${COURIER_TOKEN}" -H "Content-Type: application/json" -d '{ "courier_id": 1 }'`

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
