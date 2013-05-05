#!/bin/env python
def distance_matrix(distance_matrix):
    for distance in distance_matrix.iterkeys():
        print distance
        print distance_matrix[distance]
        print ""

def cluster(clusters):
    for _cluster in clusters:
        print _cluster

def tokens(token_weight):
    for tok_weight in token_weight.iterkeys():
        print tok_weight
        print token_weight[tok_weight]
        print ""

def enriched_tag(enriched_tags):
    for enriched in enriched_tags.iterkeys():
        print enriched
        print enriched_tags[enriched]
        print ""

def header():
    pass

def footer():
    pass
