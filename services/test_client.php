<?
try{
    $client = new SoapClient('http://localhost/WSTagger/services/test_wsdl.xml');

    $params = "Auto tagger";
    $response = $client->doHello($params);

    echo $response;

}
catch(SoapFault $e){
    var_dump($e);
}
?>
