import config
from wsdl import WSDL
def get_weight_structure(wsdl):
    all_tokens,service_tokens,operation_tokens,message_tokens,type_tokens,documentation_token=wsdl.all_tokens
    weight_service=1.0
    weight_documentation=1.0/16
    weight_operation=weight_service/(len(wsdl.operation)-1+2)
    weight_message=weight_operation/(len([ x['input'] for x in wsdl.operation ]+[ x['output'] for x in wsdl.operation ])-1+2)
    weight_type=weight_message/(len([ x['input'] for x in wsdl.operation ]+[ x['output'] for x in wsdl.operation ])-1+2)
    weight={}
    for x in documentation_token['NP']+documentation_token['VB']+documentation_token['NN']:
        weight[x]=weight_documentation
    for x in type_tokens:
        weight[x]=weight_type
    for x in message_tokens:
        weight[x]=weight_message
    for x in operation_tokens:
        weight[x]=weight_operation
    for x in service_tokens:
        weight[x]=weight_service
    return weight

def get_weight_lexical(wsdl):
    all_tokens=wsdl.all_tokens
    weight={}
    for x in all_tokens:
        if x in config.STOP_WORDS:
            weight[x]=0
        else:
            weight[x]=1
    return weight

def get_weight_frequency(wsdl,clusters):
    for sub in clusters:
        if wsdl.file_name in sub:
            cluster=sub
            break
    all_tokens_frequency={}
    all_tokens_frequency_max=-1
    for token in wsdl.all_tokens:
        all_tokens_frequency[token]=wsdl.all_tokens.count(token)
        all_tokens_frequency_max=max(all_tokens_frequency_max,wsdl.all_tokens.count(token))
    document_frequency={}
    #TODO TEST THIS
    cluster_wsdl=[]
    for x in cluster:
        try:
            cluster_wsdl.append(config.COMPUTED_WSDL[x])
        except:
            cluster_wsdl.append(WSDL(x))
    for token in wsdl.all_tokens:
        for other_wsdl in cluster_wsdl:
            if token in other_wsdl.all_tokens:
                try:
                    document_frequency[token]+=1
                except:
                    document_frequency[token]=1
    return document_frequency

