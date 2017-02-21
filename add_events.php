<?php
    require_once('/home/dneise/sandbox_db.php');
    require_once('login.php');

    $title = $_POST['title'];
    $start = $_POST['start'];
    $end = $_POST['end'];
    $role = $_POST['role'];

    try {
        $db = new PDO('mysql:host=localhost;dbname=sandbox', $user, $pass);
    } catch(Exception $e) {
        exit('Unable to connect to database.');
    }


    $sql = "INSERT INTO shift (title, start, end, role) VALUES (:title, :start, :end, :role)";
    $query = $db->prepare($sql);
    $query->execute(
        array(
            ':title'=>$title,
            ':start'=>$start,
            ':end'=>$end,
            ':role'=>$role)
    );
?>
