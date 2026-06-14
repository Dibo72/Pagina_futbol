from fastapi import APIRouter
from consultas_SQL.stats import dataBase

#todas las rutas de este archivo empiezan con este url
router = APIRouter(prefix="/Laliga/team/squad")

#creamos el objetp db para poder conectarse con el archivo que interactua con la base de datos
db = dataBase()

#rellena la url y, cuando se la llame, ejecuta la funcion definida
@router.get("/player/{player_id}")
def get_player(player_id: int):
    return db.get_playerPrueba(player_id)