import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Courier, Client, Order


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://postgres:password@localhost:5432/kzdelivery_test"
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
            'courier_id': 1
        }

        self.client_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJ4OVU2Ty0tVk1QN3NtR3lUY2wtRSJ9.eyJpc3MiOiJodHRwczovL2t6LWRlbGl2ZXJ5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTU3NTE4MDE2OTUyNDg0Njk3OSIsImF1ZCI6WyJremRlbGl2ZXJ5IiwiaHR0cHM6Ly9rei1kZWxpdmVyeS5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0MzIxNDQwLCJleHAiOjE1OTQzOTM0NDAsImF6cCI6IkdBVVZ4WTl2aG1QbTlodmxaWW55TllxMkF5aVZ3VWdPIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpvcmRlciIsImdldDpvcmRlcnNjbGllbnQiXX0.Wq3GQTJe7HzehiwCDP5CKhKPD03YPBVPT3PYzL1149O5_DMzik-LW3GiLZzmNIcqkb8Zd5SBGpaWIhx7s7jMAlKrq6Vbt4qJo3rNzVRANqmdxtBXSHWHPGzIKpqHob0xPKqpuRJbl8aX_kEjVIZDa_Un4WdMBJ-KRRDGKANNT9IDxBodSWnbeYmCsc-91D3mZC_uo9UATXgiOVIIrYpGccTKYkRKD2sfhOYWpAY5_fvkTOMaKXuzF99k0fdu_W0SBBL00OaCJ3-yMdCK00_97j1WcURjqH-YNgjAHU2ICLfLvXO85ODPCymu7ZvdNU3KAf6-B3tqNHsSU1IsitPE2A"

        self.courier_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJ4OVU2Ty0tVk1QN3NtR3lUY2wtRSJ9.eyJpc3MiOiJodHRwczovL2t6LWRlbGl2ZXJ5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzg3MzY5MjkyODU5ODk4MjIzOSIsImF1ZCI6WyJremRlbGl2ZXJ5IiwiaHR0cHM6Ly9rei1kZWxpdmVyeS5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0MzE3MDM0LCJleHAiOjE1OTQzODkwMzQsImF6cCI6IkdBVVZ4WTl2aG1QbTlodmxaWW55TllxMkF5aVZ3VWdPIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjb3VyaWVyIiwiZ2V0Om9yZGVyc2NvdXJpZXIiLCJ1cGRhdGU6b3JkZXIiXX0.qbarM676kcJIA0JAqys0JbZk4-8URcpXiB7C9r8UFY9M1s3zyvEO9mcc3c0Xnrnn3kiod3fUbN8-bPZ9B6WBFbLR42TL28w2GzfFk8VXZ10bkjaGXelxFqbk93jqYcT87v159F75LHtU0W8XyIzNDA0SHPL-BdQcb0COkuJOMDJ0RKWqDzNQ7jc59cXYB2Ulpz6yrxwfIDJpMRC63hluEatSRq7TEJivlgY5RxzMGp8A1eISrJg9oq-BJLOAadOWoixIBGF2UuEMtaHpBktnWKIRziXI_NAa71iu1DWxXoHkzqF36w3cEpo0Ulb161-y99hLzsc6WTPZtzlglCdORQ"

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
        res = self.client().post('/orders',
                                 headers={"Authorization": "Bearer {}".format(
                                     self.client_token)},
                                 json=self.new_order)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_order_id'])

    def test_if_body_not_in_request_to_create_order(self):
        res = self.client().post(
            '/orders',
            headers={
                "Authorization": "Bearer {}".format(
                    self.client_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_courier_picks_order_to_deliver(self):
        res = self.client().patch('orders/1',
                                  headers={"Authorization": "Bearer {}".format(
                                      self.courier_token)},
                                  json=self.courier_picks_order)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['courier_id'], 1)
        self.assertEqual(data['order_id'], 1)

    def test_if_body_not_in_request_to_update_order(self):
        res = self.client().patch(
            '/orders/1',
            headers={
                "Authorization": "Bearer {}".format(
                    self.courier_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_get_taken_orders_for_courier(self):
        res = self.client().get(
            '/couriers/1/orders',
            headers={
                "Authorization": "Bearer {}".format(
                    self.courier_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['orders']))

    def test_404_if_courier_does_not_exist(self):
        res = self.client().get(
            '/couriers/1000/orders',
            headers={
                "Authorization": "Bearer {}".format(
                    self.courier_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_accepted_orders_for_client(self):
        res = self.client().get(
            '/clients/1/orders',
            headers={
                "Authorization": "Bearer {}".format(
                    self.client_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['orders']))

    def test_404_if_client_does_not_exist(self):
        res = self.client().get(
            '/clients/1000/orders',
            headers={
                "Authorization": "Bearer {}".format(
                    self.client_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_courier(self):
        res = self.client().delete(
            '/couriers/1',
            headers={
                "Authorization": "Bearer {}".format(
                    self.courier_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_courier_id'], 1)

    def test_404_if_courier_does_not_exist_upon_deleting(self):
        res = self.client().delete(
            '/couriers/1000',
            headers={
                "Authorization": "Bearer {}".format(
                    self.courier_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


if __name__ == "__main__":
    unittest.main()
