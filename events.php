<?php
    require_once("db.php");
    $json = array();

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
   
    $request = "SELECT calendarentry.id, calendarentry.user_id, start, end, name as role from calendarentry join role on (calendarentry.role_id = role.id)";
    $db = create_db('sandbox');
    $result = $db->query($request) or die(print_r($db->errorInfo()));
    $calendarentries = $result->fetchAll(PDO::FETCH_ASSOC);

    $entries = array();
    foreach($calendarentries as $c)
    {
        $e = [
            "id" => $c['id'],
            "title" => $uid2name[$c['user_id']],
            "start" => $c['start'],
            "end" => $c['end'],
            "url" => "",
            "allDay" => 0,
            "role" => $c['role']
        ];
        $entries[] = $e;
    }
    echo json_encode($entries);
?>
