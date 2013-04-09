#!/bin/env python
import xml.etree.ElementTree as ET
tree=ET.parse("../services/test_wsdl.xml")
root=tree.getroot()
def operation(root):
    for child in root:
        if child.tag.split("}")[-1]=="portType":
            for child_child in child:
                print "operation:",child_child.attrib['name']
                for child_child_child in child_child:
                    if child_child_child.tag.split("}")[-1]=="documentation":
                        print "documentation:",child_child_child.text
        if child.tag.split("}")[-1]=="message":
            print "Message:",child.attrib['name']
            for child_child in child:
                print "element:",child_child.attrib['type'].split(":")[-1]
        if child.tag.split("}")[-1]=="service":
            print "Service:",child.attrib['name']



operation(root)
