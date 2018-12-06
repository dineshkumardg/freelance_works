from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'about': 'testing restful'}

	def post(self):
		return {'sent': request.get_json()}

class Divider(Resource):
	def get(self, num1, num2):
		return {'result':num1/num2}

api.add_resource(HelloWorld, '/')
api.add_resource(Divider, '/divide/<int:num1>/<int:num2>')


if __name__ == '__main__':
    app.run(debug=True)

