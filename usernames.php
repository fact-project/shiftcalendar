<?php
    require_once("db.php");
    require_once('login.php');

    $json = array();
    $query = "SELECT username, uid as user_id FROM logbook.users ORDER BY username";
    $db = create_db('factdata');
    $result = $db->query($query) or die(print_r($db->errorInfo()));
    echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));
?>
