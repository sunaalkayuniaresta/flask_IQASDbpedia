import re
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

        get_input = Preprocessing.get_input(input)
        get_query= Preprocessing.get_query(get_input)
        set_sparql = Preprocessing.set_sparql(get_query[0], get_query[1])
        send_querys = Preprocessing.send_querys(set_sparql)
        get_hasil = Preprocessing.get_hasil(send_querys)

        return {
            "get_input" : get_input,
            "get_query": get_query,
            "set_sparql": set_sparql,
            "send_querys": send_querys,
            "get_hasil": get_hasil,
        }


api.add_resource(Api, '/')

if __name__ == '__main__':
    app.run(debug=True)

