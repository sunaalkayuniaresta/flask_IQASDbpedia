import re
from SPARQLWrapper import SPARQLWrapper, XML, JSON

class Preprocessing:
    def __init__(self):
        __masukan = None
        __pekerjaan = None
        __lahir = None
        __query = None
        __resultQuery = None

    def setInput(self,masukan):
        self.__masukan = re.sub(r'[^\w]|_',' ',str(masukan.lower()))

    def getInput(self):
        return self.__masukan


    def getQuery (self):
        match = re.search('siapa nama(.*)yang', self.__masukan)
        pekerjaan = match.group(1).strip().capitalize()
        self.__pekerjaan = pekerjaan.replace(" ", "_")
        match = re.search('di (.*)', self.__masukan)
        lahir = match.group(1).strip().title()
        self.__lahir = lahir.replace(" ", "_")
        return self.__pekerjaan, self.__lahir

    def setSparQL (self):
        q1 = """
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX dbpedia-id: <http://id.dbpedia.org/resource/>
        PREFIX dbpprop-id: <http://id.dbpedia.org/resource/>


        """

        querys = q1 + """select ?name
            where {
                ?ins dbpedia-owl:occupation dbpedia-id:""" + self.__pekerjaan + """.
                ?ins rdfs:label ?name.
                ?ins dbpedia-owl:birthPlace dbpedia-id:""" + self.__lahir + """.
            }
        """

        self.__querys = querys
        return self.__querys    

    def sendQuery(self):
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(self.__querys)
        sparql.setReturnFormat(JSON)

        self.__resultQuery = sparql.query().convert()
        return self.__resultQuery

    def getHasil(self):
        hasil = []

        for x in range(len(self.__resultQuery['results']['bindings'])):
            if (self.__resultQuery['results']['bindings'][x]['name']['value'] != "" and self.__resultQuery['results']['bindings'][x]['name'][
                'value'] not in hasil):
                hasil.append(self.__resultQuery['results']['bindings'][x]['name']['value'])
        return(hasil)

    # def get_input( masukan):
    #     masukan = masukan.lower()
    #     masukan = re.sub(r'[^\w]|_',' ',str(masukan))
    #     print(masukan)
    #     return masukan

    # def get_query(masukan):
    #     match = re.search('siapa nama(.*)yang', masukan)
    #     pekerjaan = match.group(1).strip().capitalize()
    #     pekerjaan = pekerjaan.replace(" ", "_")
    #     match = re.search('di (.*)', masukan)
    #     lahir = match.group(1).strip().title()
    #     lahir = lahir.replace(" ", "_")
    #     return pekerjaan, lahir

    # def set_sparql( pekerjaan, lahir):
    #     q1 = """
    #     PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    #     PREFIX dbpedia-id: <http://id.dbpedia.org/resource/>
    #     PREFIX dbpprop-id: <http://id.dbpedia.org/resource/>


    #     """

    #     querys = q1 + """select ?name
    #         where {
    #             ?ins dbpedia-owl:occupation dbpedia-id:""" + pekerjaan + """.
    #             ?ins rdfs:label ?name.
    #             ?ins dbpedia-owl:birthPlace dbpedia-id:""" + lahir + """.
    #         }
    #     """
    #     return querys

    # def send_querys(querys):
    #     sparql = SPARQLWrapper("http://localhost:8890/sparql")
    #     sparql.setQuery(querys)
    #     sparql.setReturnFormat(JSON)

    #     results = sparql.query().convert()
    #     return results

    # def get_hasil(results):
    #     hasil = []

    #     for x in range(len(results['results']['bindings'])):
    #         if (results['results']['bindings'][x]['name']['value'] != "" and results['results']['bindings'][x]['name'][
    #             'value'] not in hasil):
    #             hasil.append(results['results']['bindings'][x]['name']['value'])
    #     return(hasil)
