<?php
    require_once("db.php");
    require_once('login.php');
    $id = $_POST['id'];
    $db = create_db('sandbox');
    $sql = "DELETE from calendarentry WHERE id=".$id;
    $query = $db->prepare($sql);
    $query->execute();
?>
