<?php

require_once("/home/dneise/sandbox_db.php");
require_once('login.php');

/* Values received via ajax */
$id = $_POST['id'];
$title = $_POST['title'];
$start = $_POST['start'];
$end = $_POST['end'];

// connection to the database
try {
 $bdd = new PDO('mysql:host=localhost;dbname=sandbox', $user, $pass);
 } catch(Exception $e) {
exit('Unable to connect to database.');
}
 // update the records
 $sql = "DELETE from shift WHERE id=".$id;
 $q = $bdd->prepare($sql);
 $q->execute();
?>

