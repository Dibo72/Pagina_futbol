<!---------------------------MENU GENERAL--------------------------->
<!--digamos que llama a una url la cual devuelve un json que se guarda en response y luego 
lo convierte en array PHP para poder usarlo con normalidad-->
<?php
$url = "http://127.0.0.1:8000/Laliga";
$response = file_get_contents($url);
$equipos = json_decode($response, true);
?>
<?php $counter = 0 ?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>LaLiga</title>
        <link rel="stylesheet" href="css/index.css">
    </head>
    <body>
        <img src="../pictures/laliga.png" alt="Logo LaLiga" class="logoLiga">
<!--esto es un formulario oculto que se autoenvia para no tener que hacer una pagina por equipo
Lo que hace es enviar datos a team.php, escondidos, manda id y el id= es para identificarlo en js-->
        <form id="formTeam" method="GET" action="team/team.php">
            <input type="hidden" name="id" id="teamId">
        </form>

<!--esto primero crea la cabecera de la tabla y despues se dan los valores de esa tabla-->
        <table border="1" cellpadding="3">
        <tr class = "principio">
            <th>Equipo</th>
            <th>PJ</th>
            <th>Diff</th>
            <th>PTS</th>
        </tr>

<!--Este foreach sirve para insertar tantos valores como equipos haya-->
        <?php foreach ($equipos as $eq): ?>
<!--Dependiendo de la posicion se le asigna una clase para poder modificarlos-->
            <?php 
                if($counter <=4){
                    $rowClass = "champions";
                }elseif ($counter <=6) {
                    $rowClass = "europa";
                }elseif($counter == 7){
                    $rowClass = "conference";
                }elseif($counter >=17){
                    $rowClass = "descenso";
                }else{
                    $rowClass = "";
                }
                ?>


<!--si clikas en un equipo manda la funcion verEquipo con el id de equipo que hayas pulsado-->
        <tr class="<?= $rowClass?>" onclick="verEquipo(<?php echo $eq['id']; ?>)" style="cursor:pointer;">
            <td>
                <img src="<?php echo $eq['logo']; ?>" alt="Logo" class="logo">
                <?php echo $eq["name"]; ?>
            </td>
            <td><?php echo $eq["matches"] ?></td>
            <td><?php echo $eq["goal_diference"] ?></td>
            <td><?php echo $eq["points"] ?></td>
            <?php $counter++ ?>
        </tr>
        <?php endforeach; ?>

        </table>
<!--esta funcion define que el teamid es el valor id dado y envia el formulario oculto-->
        <script>
        function verEquipo(id) {
            document.getElementById("teamId").value = id;
            document.getElementById("formTeam").submit();
        }
        </script>
    </body>
</html>