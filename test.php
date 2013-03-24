<?
$key="";
$query="weather";
try{
    //$client=new SoapClient("http://api.google.com/GoogleSearch.wsdl");
    $client=new SoapClient("http://localhost/WSTagger/GoogleSearch.wsdl");
    $results=$client->doGoogleSearch($key,$query,0,10,FALSE,'',FALSE,'','','');
    foreach($results->resultElements as $result){
        echo '<a href="';
        echo htmlentities($result->URL,ENT_COMPACT,'UTF-8');
        echo '">';
        echo htmlentities($result->URL,ENT_COMPACT,'UTF-8');
        echo '</a><br />';
    }

}
catch(SoapFault $e){
    echo $e->getMessage();
}
?>
