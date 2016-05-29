<?php

require_once("/home/dneise/factread_db.php");
// List of events
 $json = array();

 // Query that retrieves events
 $requete = "SELECT username FROM logbook.users ORDER BY username";

 // connection to the database
 try {
 $bdd = new PDO('mysql:host=10.0.100.21;dbname=factdata', $user, $pass);
 } catch(Exception $e) {
  exit('Unable to connect to database.');
 }
 // Execute the query
 $resultat = $bdd->query($requete) or die(print_r($bdd->errorInfo()));

 // sending the encoded result to success page
 echo json_encode($resultat->fetchAll(PDO::FETCH_ASSOC));

?>
