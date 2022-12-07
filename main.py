from SPARQLWrapper import SPARQLWrapper, XML, JSON
import re
from App import preprocessing

masukan="Siapa nama presenter yang Lahir di Jakarta? %&^[]"


valid=re.match('siapa nama(.*) yang lahir di (.*)',masukan.lower())
if valid==True:
    lower = preprocessing.get_input(preprocessing,masukan)

    pekerjaan,lahir = preprocessing.get_query(preprocessing,lower)

    query = preprocessing.set_sparql(preprocessing,pekerjaan,lahir)

    hasil_json = preprocessing.send_querys(preprocessing,query)

    value = preprocessing.get_hasil(preprocessing,hasil_json)
else:
    print("salah format")