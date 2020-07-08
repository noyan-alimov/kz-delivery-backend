import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Courier, Client, Order


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "kzdelivery_test"
        self.database_path = "postgres://postgres:password@{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # drop then create all tables
            # self.db.drop_all()
            # self.db.create_all()

        self.new_courier = {
        'name': 'John'
        }

        self.new_client = {
        'name': 'Sally'
        }

        self.new_order = {
        'item': 'document',
        'from_address': '33 str',
        'to_address': '90 str',
        'price': 30,
        'client_id': 1
        }

        self.courier_picks_order = {
        'courier_id': 2
        }

    def tearDown(self):
        pass


    def test_get_available_orders(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['orders']))

    def test_create_courier(self):
        res = self.client().post('/couriers', json=self.new_courier)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['new_courier_id'])

    def test_if_body_not_in_request_to_create_courier(self):
        res = self.client().post('/couriers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_create_client(self):
        res = self.client().post('/clients', json=self.new_client)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['new_client_id'])

    def test_if_body_not_in_request_to_create_client(self):
        res = self.client().post('/clients')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_create_order(self):
        res = self.client().post('/orders', json=self.new_order)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_order_id'])

    def test_if_body_not_in_request_to_create_order(self):
        res = self.client().post('/orders')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_courier_picks_order_to_deliver(self):
        res = self.client().patch('orders/1', json=self.courier_picks_order)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['courier_id'], 2)
        self.assertEqual(data['order_id'], 1)

    def test_if_body_not_in_request_to_update_order(self):
        res = self.client().patch('/orders/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_get_taken_orders_for_courier(self):
        res = self.client().get('/couriers/2/orders')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['orders']))

    def test_404_if_courier_does_not_exist(self):
        res = self.client().get('/couriers/1000/orders')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_accepted_orders_for_client(self):
        res = self.client().get('/clients/1/orders')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['orders']))

    def test_404_if_client_does_not_exist(self):
        res = self.client().get('/clients/1000/orders')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_courier(self):
        res = self.client().delete('/couriers/6')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_courier_id'], 6)

    def test_404_if_courier_does_not_exist_upon_deleting(self):
        res = self.client().delete('/couriers/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


if __name__ == "__main__":
    unittest.main()
