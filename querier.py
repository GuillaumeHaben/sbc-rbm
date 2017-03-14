from pymantic import sparql

class Querier():
    """Wrapper class for blazegraph-python"""
    def __init__(self, url):
        self.server = sparql.SPARQLServer(url)

    def query(self, text):
        finalQuery = ""
        prefixes = {}
        csv = "predicate,object,subject\n"
        lines = text.split("\n")
        for line in lines:
            if "PREFIX" in line:
                blocks = line.split(" ")
                prefix = blocks[1]
                uri = blocks[2].replace('<', '').replace('>', '')
                prefixes[uri] = prefix
            else:
                finalQuery = finalQuery + "\n" + line
        print "Querying server"
        result = self.server.query(text)
        for b in result['results']['bindings']:
            predicate = self.replacePrefix(b['predicate']['value'], prefixes)
            obj = self.replacePrefix(b['object']['value'], prefixes)
            subject = self.replacePrefix(b['subject']['value'], prefixes)
            csv = csv + predicate + ',' + obj + ',' + subject + '\n'
        return csv

    def replacePrefix(self, text, prefixes):
        for key in prefixes:
            text = text.replace(key, prefixes[key])
        return text
