#!/bin/env python
import xml.dom.minidom as dom
from lib import get_tokens
class WSDL():
    def __init__(self,wsdl):
        self.tree=dom.parse(wsdl)
        self.operation=self.operation()
        self.documentation=self.documentation()
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
    def get_all_tokens(self):
        service_tokens=get_tokens(self.service)
        operation_tokens=[]
        message_tokens=[]
        type_tokens=[]
        for operation in [ y for y in [ get_tokens(x['name']) for x in self.operation ] ]:
            for sub_operation in operation:
                operation_tokens.append(sub_operation)
        for message in [ x['input'] for x in self.operation ]+[ x['output'] for x in self.operation ]:
            for sub_message in message:
                message_tokens+=get_tokens(sub_message['name'])
        for _type in [ x['input'] for x in self.operation ]+[ x['output'] for x in self.operation ]:
            for sub_type in _type:
                type_tokens+=get_tokens(sub_type['type'])
        all_tokens=service_tokens+operation_tokens+message_tokens+type_tokens
        return all_tokens,service_tokens,operation_tokens,message_tokens,type_tokens
