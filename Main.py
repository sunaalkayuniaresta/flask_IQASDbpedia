from Controller.Processing import Processing
from flask import Flask, jsonify, request
from flask_restful import reqparse, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('sentence')

class Api(Resource):
    def get(self):
        input = request.args.get("sentence")

        if(input):
            processing = Processing()

            processing.setInput(input)

            getInput = processing.getInput()
            getQuery = processing.getQuery()
            setSparQL = processing.setSparQL()
            sendQuery = processing.sendQuery()
            getHasil = processing.getHasil()

            return {
                "data":{
                    "input" : input,
                    "getInput" : getInput,
                    "getQuery" : getQuery,
                    "setSparQL":setSparQL,
                    "sendQuery" : sendQuery,
                    "getHasil" : getHasil,
                    }
                }
        else:
            return {
                "message": "query sentence not found"
            }

api.add_resource(Api, '/')

if __name__ == '__main__':
    app.run(debug=True)

