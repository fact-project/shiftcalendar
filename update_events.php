<?php
    require_once("db.php");
    require_once('login.php');

    $id = $_POST['id'];
    $start = $_POST['start'];
    $end = $_POST['end'];

    $db = create_db('sandbox');
    $sql = "UPDATE calendarentry SET start=?, end=? WHERE id=?";
    $query = $db->prepare($sql);
    $query->execute(array($start, $end, $id));
?>
