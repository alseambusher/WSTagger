#!/bin/env python
WEIGHT_SERVICE=0.6
WEIGHT_OPERATION=0.4
WEIGHT_DOCUMENTATION=0

CWD="/var/www/WSTagger/"
DB=CWD+"ngd.db"

STOP_WORDS=['a','is','an','it','at','which','that','on','the','and']

SERVICES_FOLDER="services/"

CLUSTERING_WEIGHT_THRESHOLD=0.5
COMPUTED_WSDL={}
