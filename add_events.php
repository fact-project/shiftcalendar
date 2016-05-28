<?php

require_once('/home/dneise/sandbox_db.php');
require_once('login.php');

// Values received via ajax
$title = $_POST['title'];
$start = $_POST['start'];
$end = $_POST['end'];
$url = $_POST['url'];
$role = $_POST['role'];
// connection to the database
try {
$bdd = new PDO('mysql:host=localhost;dbname=sandbox', $user, $pass);
} catch(Exception $e) {
exit('Unable to connect to database.');
}

// insert the records
$sql = "INSERT INTO shift (title, start, end, url, role) VALUES (:title, :start, :end, :url, :role)";
$q = $bdd->prepare($sql);
$q->execute(array(':title'=>$title, ':start'=>$start, ':end'=>$end, ':url'=>$url, ':role'=>$role));
?>

