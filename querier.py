from pymantic import sparql

class Querier():
    """Wrapper class for blazegraph-python"""
    def __init__(self, url):
        self.server = sparql.SPARQLServer(url)
        self.prefixes = {}

    def query(self, text):
        finalQuery = ""
        args = []
        csv = ""
        lines = text.split("\n")
        for line in lines:
            if "PREFIX" in line:
                blocks = line.split(" ")
                prefix = blocks[1]
                uri = blocks[2].replace('<', '').replace('>', '')
                self.prefixes[uri] = prefix
            finalQuery = finalQuery + "\n" + line
            if "SELECT" in line:
                for word in line.split(' '):
                    if word[0] == '?':
                        args.append(word[1:])
        for arg in args:
            csv = csv + arg + ','
        csv = csv[:len(csv)-1] + '\n'
        print("Querying server")
        result = self.server.query(text)
        print("Done")
        for b in result['results']['bindings']:
            line = ""
            for arg in args:
                line = line + self.replacePrefix(b[arg]['value']) + ','
            line = line[:len(line)-1] + '\n'
            csv = csv + line
        print csv
        return csv

    def replacePrefix(self, text):
        for key in self.prefixes:
            text = text.replace(key, self.prefixes[key])
        return text
