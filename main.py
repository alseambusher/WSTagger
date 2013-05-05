import clustering
import extraction
import config
import os
import html
from wsdl import WSDL
import json

html.header()

distance_matrix=clustering.get_distance_matrix()

#prints distance matrix
html.distance_matrix(distance_matrix)

old_distance_matrix=json.dumps(distance_matrix)
if config.K_MEANS_CLUSTERING:
    clusters=clustering.get_all_clusters_k_means(distance_matrix)
else:
    clusters=clustering.get_all_clusters(distance_matrix)

#prints cluster
html.cluster(clusters)

#parse WSDL
wsdl_object_array=[]
for service in os.listdir(config.SERVICES_FOLDER):
    wsdl_object_array.append(WSDL(config.SERVICES_FOLDER+service))

#now  calculate token weight for each of the wsdl
token_weight={}
for wsdl in wsdl_object_array:
    token_weight[wsdl.file_name]=extraction.total_token_weight(wsdl,clusters)

#prints tokens
html.tokens(token_weight)


#print "\nTOKEN WEIGHT\n"
#print token_weight
#enrich tags for all wsdl
enriched_tags={}
for wsdl in wsdl_object_array:
    #enriched_tags[wsdl.file_name]=extraction.tag_enriching(wsdl,clusters,old_distance_matrix)
    enriched_tags[wsdl.file_name]=extraction.tag_enriching(wsdl,clusters,eval(old_distance_matrix))

#prints enriched tags
html.enriched_tag(enriched_tags)

html.footer()
