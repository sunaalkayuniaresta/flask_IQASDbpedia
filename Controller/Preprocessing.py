import re
from SPARQLWrapper import SPARQLWrapper, XML, JSON

class Preprocessing:
    def get_input( masukan):
        masukan = masukan.lower()
        masukan = re.sub(r'[^\w]|_',' ',str(masukan))
        print(masukan)
        return masukan

    def get_query(masukan):
        match = re.search('siapa nama(.*)yang', masukan)
        pekerjaan = match.group(1).strip().capitalize()
        pekerjaan = pekerjaan.replace(" ", "_")
        match = re.search('di (.*)', masukan)
        lahir = match.group(1).strip().title()
        lahir = lahir.replace(" ", "_")
        return pekerjaan, lahir

    def set_sparql( pekerjaan, lahir):
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

    def send_querys(querys):
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(querys)
        sparql.setReturnFormat(JSON)

        results = sparql.query().convert()
        return results

    def get_hasil(results):
        hasil = []

        for x in range(len(results['results']['bindings'])):
            if (results['results']['bindings'][x]['name']['value'] != "" and results['results']['bindings'][x]['name'][
                'value'] not in hasil):
                hasil.append(results['results']['bindings'][x]['name']['value'])
        return(hasil)
