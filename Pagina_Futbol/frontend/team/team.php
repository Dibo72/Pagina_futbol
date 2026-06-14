<!---------------------------MENU EQUIPO--------------------------->
<!--Captura el id mandado en una variable, lo manda en la url y captura el json-->
<?php
$id = $_GET['id'];

$url = "http://127.0.0.1:8000/Laliga/team/" . $id;
$response = file_get_contents($url);
$equipos = json_decode($response, true);
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title><?=  $equipos["name"] ?></title>
        <link rel="stylesheet" href="../css/index.css">
    </head>
    <body>
        <img src="../pictures/RealMadrid.png" alt="Logo Real Madrid" class="logo">

        <!--crea una tabla con los datos de ese equipo-->
        <table border="1" cellpadding="8">
        <tr>
            <td>Victorias: <?= $equipos["wins"] ?></td>
            <td>Empates: <?= $equipos["draw"] ?></td>
            <td>Derrotas: <?= $equipos["defeats"] ?></td>
            <td>Diferencia de goles: <?= $equipos["goal_diference"] ?></td>
            <td>Puntos: <?= $equipos["points"] ?></td>
        </tr>
        </table>

        <br>

        <!--Al pulsar ese boton se llama squad.php-->
        <a href="squad.php?id=<?= $id ?>" class="button">Ver plantilla</a>

        <br><br>

        <!--Al pulsar al boton llama a matches.php y le manda el id del equipo en cuestion-->
        <a href="matches.php?id=<?= $id ?>" class="button">Ver partidos</a>

        <br><br>

        <!--Al pulsar ese boton se llama index.php, es decir, vuelve hacia atras-->
        <a href="../index.php" class="button">Volver</a>
    </body>
</html>