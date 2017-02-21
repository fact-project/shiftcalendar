<?php
    function create_db($dbname)
    {
        require '/home/dneise/fact/php_credentials/all_dbs.php';
        if (array_key_exists($dbname, $all_dbs))
        {
            $host = $all_dbs[$dbname]["host"];
            $user = $all_dbs[$dbname]["user"];
            $pass = $all_dbs[$dbname]["pass"];
            $dbname = $all_dbs[$dbname]["dbname"];

            try {
                $db = new PDO(
                    'mysql:host='.$host.';dbname='.$dbname,
                    $user,
                    $pass);
                return $db;
            } catch(Exception $e) {
                exit('Unable to connect to database.');
            }
        }
        else
        {
            exit('db does not exist.');
        }
    }
?>
