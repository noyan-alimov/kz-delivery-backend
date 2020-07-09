import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from models import setup_db, Courier, Client, Order
from auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        orders = Order.query.filter_by(courier_id=None).order_by(Order.id).all()
        formatted_orders = [order.format() for order in orders]

        try:
            return jsonify({
            'success': True,
            'orders': formatted_orders
            })
        except:
            abort(400)

    @app.route('/couriers', methods=['POST'])
    def create_courier():
        body = request.get_json()
        if not body:
            abort(400)

        name = body.get('name', None)

        courier = Courier(name=name)

        try:
            courier.insert()
            return jsonify({
            'success': True,
            'new_courier_id': courier.id
            })
        except:
            courier.rollback()
            abort(422)
        finally:
            courier.close()

    @app.route('/clients', methods=['POST'])
    def create_client():
        body = request.get_json()
        if not body:
            abort(400)

        name = body.get('name', None)

        client = Client(name=name)

        try:
            client.insert()
            return jsonify({
            'success': True,
            'new_client_id': client.id
            })
        except:
            client.rollback()
            abort(422)
        finally:
            client.close()

    @app.route('/orders', methods=['POST'])
    @requires_auth('create:order')
    def create_order(token):
        body = request.get_json()
        if not body:
            abort(400)

        item = body.get('item', None)
        from_address = body.get('from_address', None)
        to_address = body.get('to_address', None)
        price = body.get('price', None)
        client_id = body.get('client_id', None)

        order = Order(item=item, from_address=from_address,
                    to_address=to_address, price=price, client_id=client_id)

        try:
            order.insert()
            return jsonify({
            'success': True,
            'new_order_id': order.id
            })
        except:
            order.rollback()
            abort(422)
        finally:
            order.close()

    @app.route('/orders/<int:order_id>', methods=['PATCH'])
    @requires_auth('update:order')
    def update_courier_picks_order(token, order_id):
        body = request.get_json()
        if not body:
            abort(400)

        courier_id = body.get('courier_id', None)

        order = Order.query.filter_by(id=order_id).first()

        try:
            order.courier_id = courier_id
            order.update()
            return jsonify({
            'success': True,
            'courier_id': courier_id,
            'order_id': order_id
            })
        except:
            order.rollback()
            abort(422)
        finally:
            order.close()


    @app.route('/couriers/<int:courier_id>/orders')
    @requires_auth('get:orderscourier')
    def get_taken_orders_for_courier(token, courier_id):
        orders = Order.query.filter_by(courier_id=courier_id).all()
        if len(orders) == 0:
            abort(404)

        formatted_orders = [order.format() for order in orders]

        try:
            return jsonify({
            'success': True,
            'orders': formatted_orders
            })
        except:
            abort(422)

    @app.route('/clients/<int:client_id>/orders')
    @requires_auth('get:ordersclient')
    def get_accepted_orders_for_client(token, client_id):
        orders = Order.query.filter_by(client_id=client_id).all()
        if len(orders) == 0:
            abort(404)

        formatted_orders = [order.format() for order in orders]

        try:
            return jsonify({
            'success': True,
            'orders': formatted_orders
            })
        except:
            abort(422)


    @app.route('/couriers/<int:courier_id>', methods=['DELETE'])
    @requires_auth('delete:courier')
    def delete_courier(token, courier_id):
        courier = Courier.query.filter_by(id=courier_id).one_or_none()
        if courier is None:
            abort(404)

        try:
            courier.delete()
            return jsonify({
            'success': True,
            'deleted_courier_id': courier_id
            })
        except:
            courier.rollback()
            abort(422)
        finally:
            courier.close()



    # Error handlers
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify(e.error), e.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
