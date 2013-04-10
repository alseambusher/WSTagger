#!/bin/env python
import xml.etree.ElementTree as ET
class WSDL():
    def __init__(self,wsdl):
        self.wsdl_tree=ET.parse(wsdl)
        self.operation=[]
        self.documentation=[]
        self.message=[]
        self.element=[]
        self.service=""
