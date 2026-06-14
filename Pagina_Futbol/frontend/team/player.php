<!---------------------------DATOS JUGADOR--------------------------->
<!--se obtiene el id del jugador y se llama la url para poder mostrar sus estadisticas-->
<?php
$id = trim($_GET["id"]);
$url = "http://127.0.0.1:8000/Laliga/team/squad/player/" . $id;
$response = file_get_contents($url);
$jugador = json_decode($response, true);
?>

<!--Se muestran las estadisticas llamando a los atributos del jugador-->
<h1><?= $jugador["nombre"] ?></h1>
<table border="1" cellpadding="8">
   <tr>
        <td>Nombre: <?= $jugador["nombre"]?></td>
        <td>Equipo: <?= $jugador["id"]?></td>
    </tr> 
</table>
 
<!--Se llama a la clase team.php y se manda el id para que carge el equipo correcto-->
<a href="squad.php?id=<?= $jugador["equipo"] ?>" class="button">Volver</a>