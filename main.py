import clustering
import extraction
import config
import os
import time
from wsdl import WSDL
import json
os.system("figlet DISTANCE MATRIX")
distance_matrix=clustering.get_distance_matrix()
for distance in distance_matrix.iterkeys():
    print distance
    print distance_matrix[distance]
    print ""
old_distance_matrix=json.dumps(distance_matrix)
clusters=clustering.get_all_clusters(distance_matrix)
os.system("figlet CLUSTERS")
time.sleep(1)
for cluster in clusters:
    print cluster

#parse WSDL
wsdl_object_array=[]
for service in os.listdir(config.SERVICES_FOLDER):
    wsdl_object_array.append(WSDL(config.SERVICES_FOLDER+service))

#now  calculate token weight for each of the wsdl
token_weight={}
for wsdl in wsdl_object_array:
    token_weight[wsdl.file_name]=extraction.total_token_weight(wsdl,clusters)
os.system("figlet TAGS")
time.sleep(1)
for tok_weight in token_weight.iterkeys():
    print tok_weight
    print token_weight[tok_weight]
    print ""


#print "\nTOKEN WEIGHT\n"
#print token_weight
#enrich tags for all wsdl
enriched_tags={}
for wsdl in wsdl_object_array:
    #enriched_tags[wsdl.file_name]=extraction.tag_enriching(wsdl,clusters,old_distance_matrix)
    enriched_tags[wsdl.file_name]=extraction.tag_enriching(wsdl,clusters,eval(old_distance_matrix))
os.system("figlet ENRICHED TAGS")
time.sleep(1)
for enriched in enriched_tags.iterkeys():
    print enriched
    print enriched_tags[enriched]
    print ""


#print "\nENRICHED TAGS\n"
#print enriched_tags

