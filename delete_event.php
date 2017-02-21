<?php
    require_once("/home/dneise/sandbox_db.php");
    require_once('login.php');

    $id = $_POST['id'];
    $title = $_POST['title'];
    $start = $_POST['start'];
    $end = $_POST['end'];

    try {
        $db = new PDO('mysql:host=localhost;dbname=sandbox', $user, $pass);
    } catch(Exception $e) {
        exit('Unable to connect to database.');
    }

    $sql = "DELETE from shift WHERE id=".$id;
    $query = $db->prepare($sql);
    $query->execute();
?>
