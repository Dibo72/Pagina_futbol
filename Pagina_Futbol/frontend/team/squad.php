<!---------------------------MENU PLANTILLA--------------------------->
<!--captura el id mandado, llama a la url con el id y se guarda el json en squad-->
<?php
$id = $_GET['id'];

$url = "http://127.0.0.1:8000/Laliga/team/" . $id . "/squad/";
$response = file_get_contents($url);
$squad = json_decode($response, true);
?>

<h1>PLANTILLA DEL EQUIPO</h1>

<!--se crea una lista con los jugadores del equipo pedido-->
<ul>
    <?php foreach ($squad["jugadores"] as $jugador): ?>
        <li>
    <!--si se pulsa en el jugador se entrae en su pantalla de estadisticas-->
            <a href="player.php?id=<?=$jugador["id"] ?>"><?= $jugador["nombre"] ?></a>
        </li>
    <?php endforeach; ?>
</ul>

<!--Se llama a la clase team.php y se manda el id para que carge el equipo correcto-->
<a href="team.php?id=<?= $id ?>" class="button">Volver</a>