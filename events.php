<?php
    require_once("/home/dneise/sandbox_db.php");
    $json = array();

    $request = "SELECT * FROM shift ORDER BY id";

    try {
        $db = new PDO('mysql:host=localhost;dbname=sandbox', $user, $pass);
    } catch(Exception $e) {
        exit('Unable to connect to database.');
    }

    $result = $db->query($request) or die(print_r($db->errorInfo()));
    echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));
?>
