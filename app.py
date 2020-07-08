import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Courier, Client, Order


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
        orders = Order.query.all()
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
        name = body.get('name', None)

        if name is None:
            abort(404)

        courier = Courier(name=name)

        try:
            courier.insert()
            return jsonify({
            'success': True,
            'created_id': courier.id
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

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
