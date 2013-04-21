import lib
import sys
from wsdl import WSDL
service1=WSDL(sys.argv[1])
service2=WSDL(sys.argv[2])
#print lib.get_tokens("cAVCsdcasd@asdva%sad1aca2AAAds3A33")
#print "".join(service.get_all_strings())
#print lib.get_tokens("%".join(service.get_all_strings()))
token1=lib.get_tokens(service1.service)
token2=lib.get_tokens(service2.service)
print lib.get_similarity(token1,token2)
