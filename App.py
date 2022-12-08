from Controller.Preprocessing import Preprocessing
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

        preprocessing = Preprocessing()

        preprocessing.setInput(input)

        getInput = preprocessing.getInput()
        getQuery = preprocessing.getQuery()
        setSparQL = preprocessing.setSparQL()
        sendQuery = preprocessing.sendQuery()
        getHasil = preprocessing.getHasil()

        return {
            "input" : input,
            "getInput" : getInput,
            "getQuery" : getQuery,
            "setSparQL":setSparQL,
            "sendQuery" : sendQuery,
            "getHasil" : getHasil,
        }


api.add_resource(Api, '/')

if __name__ == '__main__':
    app.run(debug=True)

