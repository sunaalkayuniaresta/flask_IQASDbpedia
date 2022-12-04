from SPARQLWrapper import SPARQLWrapper, XML, JSON
import re
from flask import Flask, jsonify, request
from flask_restful import reqparse, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('sentence')
# class NaturalLanguage(Resource):
#     def get(self):
#         return {'message': 'api-unsribot'}

class preprocessing(Resource):

    def get_input(self, masukan):
        masukan = masukan.lower()
        masukan = re.sub(r'[^\w]|_',' ',str(masukan))
        print(masukan)
        return masukan

    def get_query(self, masukan):
        match = re.search('siapa nama(.*)yang', masukan)
        pekerjaan = match.group(1).strip().capitalize()
        pekerjaan = pekerjaan.replace(" ", "_")
        match = re.search('di (.*)', masukan)
        lahir = match.group(1).strip().title()
        lahir = lahir.replace(" ", "_")
        return pekerjaan, lahir

    def set_sparql(self, pekerjaan, lahir):
        q1 = """
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX dbpedia-id: <http://id.dbpedia.org/resource/>
        PREFIX dbpprop-id: <http://id.dbpedia.org/resource/>


        """

        querys = q1 + """select ?name
            where {
                ?ins dbpedia-owl:occupation dbpedia-id:""" + pekerjaan + """.
                ?ins rdfs:label ?name.
                ?ins dbpedia-owl:birthPlace dbpedia-id:""" + lahir + """.
            }
        """
        return querys

    def send_querys(self,querys):
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(querys)
        sparql.setReturnFormat(JSON)

        results = sparql.query().convert()
        return results

    def get_hasil(self,results):
        hasil = []

        for x in range(len(results['results']['bindings'])):
            if (results['results']['bindings'][x]['name']['value'] != "" and results['results']['bindings'][x]['name'][
                'value'] not in hasil):
                hasil.append(results['results']['bindings'][x]['name']['value'])
        return(hasil)

    def get(self):
        input = request.args.get("sentence")

        langkah1 = self.get_input(input)
        langkah2= self.get_query(langkah1)
        langkah3 = self.set_sparql(langkah2[0], langkah2[1])
        langkah4 = self.send_querys(langkah3)
        langkah5 = self.get_hasil(langkah4)
        print("=============================langkah5", langkah5)

        # result = self.get_hasil(
        #     self.send_querys(
        #         self.set_sparql(
        #             self.get_query(
        #                 self.get_input(input)),pekerjaan,lahir)))

        return {
            "langkah1" : langkah1,
            "langkah2": langkah2,
            "langkah3": langkah3,
            "langkah4": langkah4,
            "langkah5": langkah5,
        }


api.add_resource(preprocessing, '/')

if __name__ == '__main__':
    app.run(debug=True)

