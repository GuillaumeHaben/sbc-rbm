from tsv import DictReader

trainingSetFile = open("sets/training_set_91_91.tsv")
trainingSet = DictReader(trainingSetFile)
print(trainingSet)
trainingSet.close()
