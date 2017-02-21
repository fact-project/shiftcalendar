<?php
    require_once("db.php");
    $json = array();

    $request = "SELECT * FROM shift ORDER BY id";
    $db = create_db('sandbox');
    $result = $db->query($request) or die(print_r($db->errorInfo()));
    echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));
?>
