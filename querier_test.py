from querier import Querier
import csv
import time
start_time = time.time()

url = 'http://127.0.0.1:9999/bigdata/sparql'

prefix = """
PREFIX atc: <http://bio2rdf.org/atc:>
PREFIX bio2rdfv: <http://bio2rdf.org/bio2rdf_vocabulary:>
PREFIX clinvar: <http://bio2rdf.org/clinvar:>
PREFIX clinvarv: <http://bio2rdf.org/clinvar_vocabulary:>
PREFIX dbv: <http://bio2rdf.org/drugbank_vocabulary:>
PREFIX dbr: <http://bio2rdf.org/drugbank_resource:>
PREFIX disgenet: <http://rdf.disgenet.org/resource/gda/>
PREFIX drugbank: <http://bio2rdf.org/drugbank:>
PREFIX mapping: <http://biodb.jp/mappings/>
PREFIX medispan: <http://orpailleur.fr/medispan/>
PREFIX ncbigene: <http://bio2rdf.org/ncbigene:>
PREFIX pharmgkb: <http://bio2rdf.org/pharmgkb:>
PREFIX pharmgkbv: <http://bio2rdf.org/pharmgkb_vocabulary:>
PREFIX pubchemcompound: <http://bio2rdf.org/pubchem.compound:>
PREFIX sider: <http://bio2rdf.org/sider:>
PREFIX siderv: <http://bio2rdf.org/sider_vocabulary:>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX so: <http://bio2rdf.org/sequence_ontology:>
PREFIX umls: <http://bio2rdf.org/umls:>
PREFIX uniprot: <http://bio2rdf.org/uniprot:>
"""

query1 = """
SELECT DISTINCT ?mediSpanDrug ?mediSpanDisease

WHERE {
  ?mediSpanDrug medispan:indication ?mediSpanDisease
}
"""

query2 = """
SELECT DISTINCT ?mediSpanDrug ?mediSpanDisease

WHERE {
  ?mediSpanDrug medispan:side_effect ?mediSpanDisease
}
"""

query3 = """
SELECT DISTINCT ?siderDrug ?siderDisease

WHERE {
  ?siderDrug siderv:indication ?siderDisease
}
"""

# Vide a priori
query4 = """
SELECT DISTINCT ?siderDrug ?siderDisease

WHERE {
  ?siderDrug siderv:side_effect ?siderDisease 
}
"""

# Renvoie une erreur
query5 = """
SELECT DISTINCT ?disGenetVariant ?disGenetDisease

WHERE {
  ?disGenetVariant sio:SIO_000628 ?disGenetDisease 
}
"""

query6 = """
SELECT DISTINCT ?clinvarVariant ?disGenetDisease

WHERE {
  ?clinvarVariant clinvarv:Variant_Phenotype ?disGenetDisease
}
"""

# Vide a priori
query7 = """
SELECT DISTINCT ?clinvarVariant ?disGenetDisease

WHERE {
  ?clinvarVariant clinvar:x-medgen ?disGenetDisease
}
"""

localQuerier = Querier(url)

# resultQuery1 = localQuerier.query(prefix+query1)
# csvFile1 = open("csvFile1.csv", 'w')
# csvFile1.write(resultQuery1)
# print "[Running Time] %s sec" % (time.time() - start_time)

# resultQuery2 = localQuerier.query(prefix+query2)
# csvFile2 = open("csvFile2.csv", 'w')
# csvFile2.write(resultQuery2)
# print "[Running Time] %s sec" % (time.time() - start_time)

# resultQuery3 = localQuerier.query(prefix+query3)
# csvFile3 = open("csvFile3.csv", 'w')
# csvFile3.write(resultQuery3)
# print "[Running Time] %s sec" % (time.time() - start_time)

# resultQuery4 = localQuerier.query(prefix+query4)
# csvFile4 = open("csvFile4.csv", 'w')
# csvFile4.write(resultQuery4)
# print "[Running Time] %s sec" % (time.time() - start_time)

# resultQuery5 = localQuerier.query(prefix+query5)
# csvFile5 = open("csvFile5.csv", 'w')
# csvFile5.write(resultQuery5)
# print "[Running Time] %s sec" % (time.time() - start_time)

resultQuery6 = localQuerier.query(prefix+query6)
csvFile6 = open("csvFile6.csv", 'w')
csvFile6.write(resultQuery6)
print "[Running Time] %s sec" % (time.time() - start_time)

resultQuery7 = localQuerier.query(prefix+query7)
csvFile7 = open("csvFile7.csv", 'w')
csvFile7.write(resultQuery7)
print "[Running Time] %s sec" % (time.time() - start_time)


# with open('csvFile1.csv') as csvFile1:
# 	reader1 = csv.DictReader(csvFile1)
# with open('csvFile2.csv') as csvFile2:
# 	reader2 = csv.DictReader(csvFile2)
# with open('csvFile3.csv') as csvFile3:
# 	reader3 = csv.DictReader(csvFile3)
# with open('csvFile4.csv') as csvFile4:
# 	reader4 = csv.DictReader(csvFile4)
# # with open('csvFile5.csv') as csvFile5:
# # 	reader5 = csv.DictReader(csvFile5)
# with open('csvFile6.csv') as csvFile6:
# 	reader6 = csv.DictReader(csvFile6)
# with open('csvFile7.csv') as csvFile7:
# 	reader7 = csv.DictReader(csvFile7)
