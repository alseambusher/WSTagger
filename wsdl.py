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
        for portType in self.getElementsByTagName(self.tree,"portType"):
            port={}
            port['name']=portType.getAttributeNode("name").nodeValue
            for operation in self.getElementsByTagName(portType,"operation"):
                input_message=self.getElementsByTagName(operation,"input")[0].getAttributeNode("message").nodeValue.split(":")[-1]
                output_message=self.getElementsByTagName(operation,"output")[0].getAttributeNode("message").nodeValue.split(":")[-1]
                port['input']=self.getElementsByMessage(input_message)
                port['output']=self.getElementsByMessage(output_message)
            data.append(port)
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
    #this returns all the inputs/outputs corresponding to a message in WSDL
    def getElementsByMessage(self,message):
        data=[]
        for message_element in self.getElementsByTagName(self.tree,"message"):
            if message_element.getAttributeNode("name").nodeValue == message:
                for part in self.getElementsByTagName(message_element,"part"):
                    part_data={}
                    part_data['name']=part.getAttributeNode("name").nodeValue
                    part_data['type']=part.getAttributeNode("type").nodeValue.split(":")[-1]
                    data.append(part_data)
        return data
    def get_all_strings(self):
        data=[]
        for x in self.operation:
            #TODO FIX THIS
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
