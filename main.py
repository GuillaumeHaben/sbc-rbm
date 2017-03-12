from tsv import DictReader
from rbm import RBM, np

geneSet = set()
drugSet = set()

trainingSetFile = open("sets/training_set_91_91.tsv")
trainingSet = DictReader(trainingSetFile)

for row in trainingSet:
    geneSet.add(row['gene'])
    drugSet.add(row['drug'])

geneList = list(geneSet)
drugList = list(drugSet)

trainingData = [[0 for i in range(len(drugList))] for j in range(len(geneList))]

for row in trainingSet:
    geneIndex = geneList.index(row['gene'])
    drugIndex = drugList.index(row['drug'])
    associatied = {'associated': 1, 'not associated': 0}.get(row['association'])
    trainingData[geneIndex][drugIndex] = associatied

rbm = RBM(num_visible=len(drugList), num_hidden=8)
rbm.train(np.array(trainingData), max_epochs = 300)

print(rbm.run_hidden(np.array([[1,0,1,0,0,1,1,0]])))

trainingSet.close()
