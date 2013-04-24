import nltk
def get_sentence(document):
    sentences=nltk.sent_tokenize(document)
    sentences=[nltk.word_tokenize(sent) for sent in sentences]
    sentences=[nltk.pos_tag(sent) for sent in sentences][0]
    #TODO change this grammar
    grammar="NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    #returns a tree and an array
    return cp.parse(sentences),sentences

def get_noun_phrase_tree(myTree, phrase="NP"):
    myPhrases = []
    if (myTree.node == phrase):
        myPhrases.append( myTree.copy(True) )
    for child in myTree:
        if (type(child) is nltk.tree.Tree):
            list_of_phrases = get_noun_phrase_tree(child, phrase)
            if (len(list_of_phrases) > 0):
                myPhrases.extend(list_of_phrases)
    return myPhrases

def lexical_analyzer(string):
    data={'NP':[],'NN':[],'VB':[]}
    if not string:
        return data
    sentence_tree,sentence=get_sentence(string)
    myPhrases=get_noun_phrase_tree(sentence_tree)
    NP=[]
    for phrase in myPhrases:
        NP.append("")
        for word in phrase:
            NP[-1]+=" "+word[0]
        NP[-1]=NP[-1][1:]
    data['NP']=NP
    data['NN']=[ x for (x,y) in sentence if y[0]=="N" ]
    data['VB']=[ x for (x,y) in sentence if y[0]=="V" ]
    return data
def get_weight_structure(wsdl):
    all_tokens,service_tokens,operation_tokens,message_tokens,type_tokens=wsdl.get_all_tokens()[:-1]
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
    all_tokens,service_tokens,operation_tokens,message_tokens,type_tokens,documentation_token=wsdl.get_all_tokens()[:-1]
