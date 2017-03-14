from csv import DictReader
from rbm import RBM, np

TRAINING_SAMPLE_SIZE = 100

localQuerier = Querier('http://127.0.0.1:9999/bigdata/sparql')
localPropertyFinder = PropertyFinder(localQuerier)

effectsList = [0, 0, 0]

csvFile = open("result.tsv")
trainingSet = DictReader(csvFile)[:TRAINING_SAMPLE_SIZE]

trainingRows = []
trainingData = [[0 for i in range(len(effectsList))] for j in range(TRAINING_SAMPLE_SIZE)]

for row in trainingSet:
    geneProperties = DictReader(localPropertyFinder.findGeneProperties(row['gene']))
    # TODO: trouver les index
    # - Pour chaque dictionnaire de geneProperties, trouver son indice dans effectsList
    # - trainingData[indice de row][indice du dico] = 1
    drugProperties = DictReader(localPropertyFinder.findDrugProperties(row['drug']))
    # TODO: idem


rbm = RBM(num_visible=len(effectsList), num_hidden=30)
rbm.train(np.array(trainingData), max_epochs = 300)

trainingSet.close()
