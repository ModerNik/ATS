<?php

$host='localhost';
$database='main_data';
$user='root';
$pswd='1234';
 
$dbh = mysql_connect($host, $user, $pswd) or die("Не могу соединиться с MySQL.");
mysql_select_db($database) or die("Не могу подключиться к базе.");

if (isset($_POST["find_group"])) { 
	$query = "SELECT * FROM '.$_POST["find_group"].'";
	$res = mysql_query($query);
	//while($row = mysql_fetch_array($res)){
	//echo .$row['name']."<br>\n"; }
    	($row = mysql_fetch_array($res)
    	echo json_encode($row); 
}

?>