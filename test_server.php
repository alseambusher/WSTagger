<?php
ini_set("soap.wsdl_cache_enabled","0");
$server = new SoapServer("test_wsdl.xml");

function doHello($yourName){


  return "Hello, ".$yourName;
}

$server->AddFunction("doHello");
$server->handle();
?>
