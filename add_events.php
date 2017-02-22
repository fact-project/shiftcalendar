<?php
    require_once('db.php');
    require_once('login.php');

    $user_id = $_POST['user_id'];
    $role_id = $_POST['role_id'];
    $start = $_POST['start'];
    $end = $_POST['end'];

    $db = create_db('sandbox');
    $sql = "INSERT INTO calendarentry (user_id, role_id, start, end) VALUES (:user_id, :role_id, :start, :end)";
    $query = $db->prepare($sql);
    $query->execute(
        array(
            ':user_id'=>$user_id,
            ':role_id'=>$role_id,
            ':start'=>$start,
            ':end'=>$end
        )
    );
?>