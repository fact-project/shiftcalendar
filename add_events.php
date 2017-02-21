<?php
    require_once('db.php');
    require_once('login.php');

    $title = $_POST['title'];
    $start = $_POST['start'];
    $end = $_POST['end'];
    $role = $_POST['role'];

    $db = create_db('sandbox');
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
