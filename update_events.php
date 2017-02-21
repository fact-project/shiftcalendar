<?php
    require_once("db.php");
    require_once('login.php');

    $id = $_POST['id'];
    $title = $_POST['title'];
    $start = $_POST['start'];
    $end = $_POST['end'];

    $db = create_db('sandbox');
    $sql = "UPDATE shift SET title=?, start=?, end=? WHERE id=?";
    $query = $db->prepare($sql);
    $query->execute(array($title, $start, $end, $id));
?>
