#!/bin/env python
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
        for operation in self.getElementsByTagName(self.tree,"operation"):
            try:
                data.append(operation.getAttributeNode("name").nodeValue)
            except:
                pass
        return data
    def documentation(self):
        data=[]
        for document in self.getElementsByTagName(self.tree,"documentation"):
            try:
                data.append(document.firstChild.data)
            except:
                pass
        return data
    def message(self):
        data=[]
        for message in self.getElementsByTagName(self.tree,"message"):
            name=message.getAttributeNode("name").nodeValue
            attribute=[]
            for part in self.getElementsByTagName(message,"part"):
                attribute.append(part.getAttributeNode("type").nodeValue.split(":")[-1])
            data.append({'name':name,'attribute':attribute})
        return data
    def elements(self):
        data=[]
        for element in self.getElementsByTagName(self.tree,"element"):
            data.append(element.getAttributeNode("name").nodeValue)
        return data
    def service(self):
        return self.getElementsByTagName(self.tree,"service")[0].getAttributeNode("name").nodeValue
    def getElementsByTagName(self,node,tag):
        #return node.getElementsByTagName(tag)+node.getElementsByTagName("xsd:"+tag)+node.getElementsByTagName("wsdl:"+tag)+node.getElementsByTagName("wsdlsoap:"+tag)
        return node.getElementsByTagName(tag)+node.getElementsByTagName("xsd:"+tag)+node.getElementsByTagName("wsdl:"+tag)
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
