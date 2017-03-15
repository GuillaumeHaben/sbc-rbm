from csv import DictReader
from rbm import RBM, np
from querier import Querier
from propertyFinder import PropertyFinder

TRAINING_SAMPLE_SIZE = 100

localQuerier = Querier('http://127.0.0.1:9999/bigdata/sparql')
localPropertyFinder = PropertyFinder(localQuerier)

effectsList = [{'effect': "", 'disease': ""}]

csvFile = open("result.tsv")
trainingSet = DictReader(csvFile)[:TRAINING_SAMPLE_SIZE]

trainingRows = []
trainingData = [[0 for i in range(len(effectsList))] for j in range(TRAINING_SAMPLE_SIZE)]

for index1, row in trainingSet:
    geneProperties = DictReader(localPropertyFinder.findGeneProperties(row['gene']))
    for prop in geneProperties:
        for index2, item in effectsList:
            if prop == item:
                trainingData[index1][index2] = 1
    drugProperties = DictReader(localPropertyFinder.findDrugProperties(row['drug']))
    for prop in drugProperties:
        for index2, item in effectsList:
            if prop == item:
                trainingData[index1][index2] = 1

rbm = RBM(num_visible=len(effectsList), num_hidden=30)
rbm.train(np.array(trainingData), max_epochs = 300)

trainingSet.close()
