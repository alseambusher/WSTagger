import config
def get_weight_structure(wsdl):
    all_tokens,service_tokens,operation_tokens,message_tokens,type_tokens=wsdl.get_all_tokens()
    weight_service=1.0
    weight_operation=weight_service/(len(wsdl.operation)-1+2)
    weight_message=weight_operation/(len([ x['input'] for x in wsdl.operation ]+[ x['output'] for x in wsdl.operation ])-1+2)
    weight_type=weight_message/(len([ x['input'] for x in wsdl.operation ]+[ x['output'] for x in wsdl.operation ])-1+2)
    weight={}
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
    all_tokens=list(set(wsdl.get_all_tokens()[0]))
    for token in all_tokens:
        if token in config.STOP_WORDS:
            all_tokens.remove(token)
