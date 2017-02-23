<?php
    require_once("db.php");

    $db = create_db('factdata');
    $request = "SELECT username, uid FROM logbook.users";
    $result = $db->query($request) or die(print_r($db->errorInfo()));
    $user2id = array();
    $uid2name = array();
    foreach($result->fetchAll(PDO::FETCH_ASSOC) as $u)
    {
        $user2id[$u['username']] = $u['uid'];
        $uid2name[$u['uid']] = $u['username'];
    }
?>
