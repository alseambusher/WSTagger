import clustering
import extraction
import config
import os
from wsdl import WSDL

distance_matrix=clustering.get_distance_matrix()
clusters=clustering.get_all_clusters(distance_matrix)

#parse WSDL
wsdl_object_array=[]
for service in os.listdir(config.SERVICES_FOLDER):
    wsdl_object_array.append(WSDL(config.SERVICES_FOLDER+service))

#enrich tags for all wsdl
enriched_tags={}
for wsdl in wsdl_object_array:
    enriched_tags[wsdl.file_name]=extraction.tag_enriching(wsdl,clusters,distance_matrix)

#now  calculate token weight for each of the wsdl
token_weight={}
for wsdl in wsdl_object_array:
    token_weight[wsdl.file_name]=extraction.total_token_weight(wsdl,clusters)

print enriched_tags
print token_weight
