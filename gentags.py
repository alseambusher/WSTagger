import lib
import sys
from wsdl import WSDL
service=WSDL(sys.argv[1])
#print lib.get_tokens("cAVCsdcasd@asdva%sad1aca2AAAds3A33")
#print "".join(service.get_all_strings())
print lib.get_tokens("".join(service.get_all_strings()))
