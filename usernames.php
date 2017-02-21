<?php
	require_once("/home/dneise/factread_db.php");
	require_once('login.php');

	$json = array();
	$query = "SELECT username FROM logbook.users ORDER BY username";

	try {
	 	$db = new PDO('mysql:host=10.0.100.21;dbname=factdata', $user, $pass);
	} catch(Exception $e) {
	  	exit('Unable to connect to database.');
	}
	$result = $db->query($query) or die(print_r($db->errorInfo()));

	echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));
?>
