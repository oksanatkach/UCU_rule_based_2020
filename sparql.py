from SPARQLWrapper import SPARQLWrapper, JSON

def get_country_description():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(
        "PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>"
        "SELECT DISTINCT ?citylabel ?pop"
        "WHERE {"
            "?city rdf:type dbpedia-owl:City."
            "?city rdfs:label ?citylabel."
            "?city dbpedia-owl:populationTotal ?pop ."
            "FILTER (lang(?citylabel) = 'en' and ?pop>10000)"
        "}"
                    )

    return sparql.query().convert()

jsn = get_country_description()['results']['bindings']
cities = [el['citylabel']['value'].split(', ')[0] for el in jsn]
cities.sort()
with open('cities.lst', 'w') as f:
    for el in cities:
        f.write(el.encode('utf-8') + '\n')
