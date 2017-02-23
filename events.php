<?php
    require_once("db.php");
    require_once("username_userid_maps.php");
    $start = $_GET['start'];
    if (!$start) {
        $start="2011-01-01";
    }
    $end = $_GET['end'];
    if (!$end) {
       $end = "2100-01-01";
    }

    $request = 'SELECT calendarentry.id, calendarentry.user_id, start, end, role.id as role_id from calendarentry join role on (calendarentry.role_id = role.id) where start>="'.$start.'" and end<="'.$end.'"';
    $db = create_db('sandbox');
    $result = $db->query($request) or die(print_r($db->errorInfo()));
    $calendarentries = $result->fetchAll(PDO::FETCH_ASSOC);

    foreach($calendarentries as &$c)
    {
        $c["url"] = "";
        $c["allDay"] = 0;
        $c["title"] = $uid2name[$c['user_id']];
    }
    echo json_encode($calendarentries);
?>
