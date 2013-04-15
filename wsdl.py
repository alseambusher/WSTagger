#!/bin/env python
#TODO put try catch blocks
#TODO take care of schemas
import xml.dom.minidom as dom
class WSDL():
    def __init__(self,wsdl):
        self.tree=dom.parse(wsdl)
        self.operation=self.operation()
        self.documentation=self.documentation()
        self.message=self.message()
        self.elements=self.elements()
        self.service=self.service()
    def operation(self):
        data=[]
        for operation in self.tree.getElementsByTagName("operation"):
            data.append(operation.getAttributeNode("name").nodeValue)
        return data
    def documentation(self):
        data=[]
        for document in self.tree.getElementsByTagName("documentation"):
            data.append(document.firstChild.data)
        return data
    def message(self):
        data=[]
        for message in self.tree.getElementsByTagName("message"):
            name=message.getAttributeNode("name").nodeValue
            attribute=[]
            for part in message.getElementsByTagName("part"):
                attribute.append(part.getAttributeNode("type").nodeValue.split(":")[-1])
            data.append({'name':name,'attribute':attribute})
        return data
    def elements(self):
        data=[]
        for element in self.tree.getElementsByTagName("xsd:element"):
            data.append(element.getAttributeNode("name").nodeValue)
        return data
    def service(self):
        return self.tree.getElementsByTagName("service")[0].getAttributeNode("name").nodeValue
    def get_all_strings(self):
        data=[]
        for x in self.operation:
            data.append(x)
        for x in self.documentation:
            data.append(x)
        for x in self.message:
            data.append(x['name'])
            for y in x['attribute']:
                data.append(y)
        for x in self.elements:
            data.append(x)
        data.append(self.service)
        return data
