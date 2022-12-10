import re
# from SPARQLWrapper import SPARQLWrapper, XML, JSON
from Model.SparQL import SparQL

class Processing:
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
        self.__querys = SparQL.setQuery(self.__pekerjaan, self.__lahir)
        return self.__querys    

    def sendQuery(self):
        self.__resultQuery = SparQL.queryToDB(self.__querys)
        return self.__resultQuery

    def getHasil(self):
        hasil = []

        for x in range(len(self.__resultQuery['results']['bindings'])):
            if (self.__resultQuery['results']['bindings'][x]['name']['value'] != "" and self.__resultQuery['results']['bindings'][x]['name'][
                'value'] not in hasil):
                hasil.append(self.__resultQuery['results']['bindings'][x]['name']['value'])
        return(hasil)