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

def get_tokens(string):
    string=string.replace("@","%").replace("_","%")
    for char in range(ord('A'),ord('Z')+1):
        string=string.replace(chr(char),"%"+chr(char))
    print string
    for num in range(0,10):
        string=string.replace(str(num),"%"+str(num))
    tokens=filter(None,string.split("%"))
    #merge CAPS
    caps=""
    delete_tokens=[]
    for i in range(0,len(tokens)):
        try:
            if not caps and len(tokens[i])==1 and tokens[i] in [ chr(x) for x in range(ord("A"),ord("Z")+1) ]:
                caps=tokens[i]
            elif caps and tokens[i][0] in [ chr(x) for x in range(ord("A"),ord("Z")+1) ]:
                delete_tokens.append(tokens[i-1])
                tokens[i]=tokens[i-1]+tokens[i]
            else:
                caps=""
        except:
            pass

    #now merge numbers
    num=None
    for i in range(0,len(tokens)):
        try:
            if not num and len(tokens[i])==1 and tokens[i] in [ str(x) for x in range(0,10) ]:
                num=tokens[i]
            elif num and tokens[i][0] in [ str(x) for x in range(0,10) ]:
                delete_tokens.append(tokens[i-1])
                tokens[i]=tokens[i-1]+tokens[i]
            else:
                num=None
        except:
            pass



    for delete in delete_tokens:
        tokens.remove(delete)
    return tokens

print get_tokens("cAVCsdcasd@asdva%sad1aca2AAAds3A33")
#operation(root)
