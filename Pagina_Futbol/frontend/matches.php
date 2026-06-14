<?php
$id = $_GET["id"];

$url = "http://127.0.0.1:8000/Laliga/team/" . $id . "/matches/";
$response = file_get_contents($url);
$matches = json_decode($response, true);
?>