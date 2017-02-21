<?php
    require_once("db.php");
    require_once('login.php');

    $id = $_POST['id'];
    $title = $_POST['title'];
    $start = $_POST['start'];
    $end = $_POST['end'];

    $db = create_db('sandbox');
    $sql = "DELETE from shift WHERE id=".$id;
    $query = $db->prepare($sql);
    $query->execute();
?>
