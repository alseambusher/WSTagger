<?
try{
    $client = new SoapClient('test_wsdl.xml');

    $params = "Auto tagger";
    $response = $client->doHello($params);

    echo $response;

}
catch(SoapFault $e){
    var_dump($e);
}
?>
