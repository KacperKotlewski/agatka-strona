<?php
if(session_status() != 2){
    session_start();
}
echo '
<!DOCTYPE html>
<html lang="pl">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://kit.fontawesome.com/81686d98c9.js" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css?family=Exo|Exo+2&subset=latin,latin-ext" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="style/main/main.css">
<link rel="stylesheet" type="text/css" href="style/main/imageLib.css">
<link rel="stylesheet" type="text/css" href="style/main/topMenu.css">
<link rel="stylesheet" type="text/css" href="style/main/lightMode.css">
<link rel="stylesheet" type="text/css" href="style/ajax/gallery.css">
<link rel="stylesheet" type="text/css" href="other/fontello/css/fontello.css">
<script src="js/darkmode.js"></script>
<script src="js/menuMobileButton.js"></script>
<script src="js/onresize.js"></script>
<script src="js/onload.js"></script>
<script src="js/ajaxGalleryMenager.js"></script>
<script src="js/scrollTo.js"></script>
';
include_once "../php/func/function.php";
include_once "../php/SQL/checkTables.php";
?>