#!/bin/env python
import math
from basic import gsearch
def get_tokens(string):
    #remove spaces in begining and ending places
    string=str(string).strip().replace("\n"," ")
    string=string.replace("@","%").replace("_","%").replace(" ","%")
    for char in range(ord('A'),ord('Z')+1):
        string=string.replace(chr(char),"%"+chr(char))
    for num in range(0,10):
        string=string.replace(str(num),"%"+str(num))
    tokens=string.split("%")
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
            caps=""

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
    #remove duplicates and nulls and return
    return filter(None,list(set(tokens)))

#similarity
def get_similarity(Vs1,Vs2):
    sum_=0
    for t1 in Vs1:
        for t2 in Vs2:
            sum_+=1-get_NGD(t1,t2)
    return sum_/(len(Vs1)*len(Vs2))

#NGD
def get_NGD(string1,string2):
    print string1,string2
    m = 45000000000
    n0 = int(gsearch(string1)['cursor']['estimatedResultCount'])
    n1 = int(gsearch(string2)['cursor']['estimatedResultCount'])
    n2 = int(gsearch(string1+" "+string2)['cursor']['estimatedResultCount'])
    print n0,n1,n2
    l1 = max(math.log10(n0),math.log10(n1))-math.log10(n2)
    l2 = math.log10(m)-min(math.log10(n0),math.log10(n1))
    return l1/l2
