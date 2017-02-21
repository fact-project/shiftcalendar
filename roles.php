<?php
    require_once("db.php");

    $json = array();
    $query = "SELECT * FROM roles";
    $db = create_db('sandbox');
    $result = $db->query($query) or die(print_r($db->errorInfo()));
    echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));
?>
