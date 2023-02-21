from SPARQLWrapper import SPARQLWrapper, JSON

class SparQL:
    def setQuery(pekerjaanParam, lahirParam):
        return  """
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX dbpedia-id: <http://id.dbpedia.org/resource/>
        PREFIX dbpprop-id: <http://id.dbpedia.org/resource/>
            
            select ?name
            where {
                ?ins dbpedia-owl:occupation dbpedia-id:%s.
                ?ins rdfs:label ?name.
                ?ins dbpedia-owl:birthPlace dbpedia-id:%s.
            }
        """%(pekerjaanParam, lahirParam)

    def queryToDB(queryParam):
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(queryParam)
        sparql.setReturnFormat(JSON)

        resultQuery = sparql.query().convert()
        return resultQuery

