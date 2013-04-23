import config
from lib import get_NGD,get_tokens
#get similarity
def get_similarity(Vs1,Vs2):
    sum_=0
    for t1 in Vs1:
        for t2 in Vs2:
            sum_+=1-get_NGD(t1,t2)
    try:
        return sum_/(len(Vs1)*len(Vs2))
    except ZeroDivisionError:
        return 0

#similarity for service name / operation name /element name/ documentation
def get_similarity_name(name1,name2):
    return get_similarity(get_tokens(name1),get_tokens(name2))

#this gives the similarity of input/output types using operation
def get_similarity_type(operation1,operation2,_type="input"):
    operation1_types=[]
    operation2_types=[]
    for _input in operation1[_type]:
        for token in get_tokens(_input['type']):
            operation1_types.append(token.lower())
    for _input in operation2[_type]:
        for token in get_tokens(_input['type']):
            operation2_types.append(token.lower())

    # we are removing all 'type' in tokens
    O1_intersection_O2=len(filter(set(operation1_types).__contains__,operation2_types))
    try:
        return (2*O1_intersection_O2)/(len(operation1_types)+len(operation2_types))
    except:
        return 0

#this gives similarity of i/o names of elements in operation
def get_similarity_element(operation1,operation2,_type="input"):
    operation1_element=[]
    operation2_element=[]
    for _input in operation1[_type]:
        for token in get_tokens(_input['name']):
            operation1_element.append(token.lower())
    for _input in operation2[_type]:
        for token in get_tokens(_input['name']):
            operation2_element.append(token.lower())

    return get_similarity(operation1_element,operation2_element)

def get_similarity_input_output(operation1,operation2,_type="input"):
    return 0.5*(get_similarity_type(operation1,operation2,_type)+get_similarity_element(operation1,operation2,_type))

#pass array of operations
def get_similarity_operation(operationSet1,operationSet2):
    _sum=0
    for operation in operationSet1:
        _sum+=max([ 0.4*get_similarity_name(x['name'],operation['name'])+0.3*get_similarity_input_output(x,operation)+0.3*get_similarity_input_output(x,operation,"output") for x in operationSet2])
    for operation in operationSet2:
        _sum+=max([ 0.4*get_similarity_name(x['name'],operation['name'])+0.3*get_similarity_input_output(x,operation)+0.3*get_similarity_input_output(x,operation,"output") for x in operationSet1])
    return _sum

def similarity_wsdl(wsdl1,wsdl2):
    return config.WEIGHT_SERVICE*get_similarity_name(wsdl1.service,wsdl2.service
                                                     )+config.WEIGHT_OPERATION* get_similarity_operation(wsdl1.operation,wsdl2.operation
                                                                                                         )+config.WEIGHT_DOCUMENTATION* get_similarity_name(wsdl1.documentation,wsdl2.documentation)
