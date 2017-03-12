class DictReader(list):
    """Parses TSV files into arrays of dictionnaries"""
    def __init__(self, tsvFile):
        self.tsvFile = tsvFile
        self.attributes = tsvFile.readline().replace('\n', '').split('\t')
        for line in tsvFile.readlines():
            row = {}
            for i in range(len(self.attributes)):
                row[self.attributes[i]] = line.replace('\n', '').split('\t')[i]
            self.append(row)

    def close(self):
        self.tsvFile.close()
        self.tsvFile = None
