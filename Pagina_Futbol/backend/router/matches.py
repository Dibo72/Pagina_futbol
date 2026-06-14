from fastapi import APIRouter
from consultas_SQL.stats import dataBase

#todas las rutas de este archivo empiezan con este url
router = APIRouter(prefix="/Laliga")

#creamos el objetp db para poder conectarse con el archivo que interactua con la base de datos
db = dataBase()

#rellena la url y, cuando se la llame, ejecuta la funcion definida
@router.get("/team/{team_id}/matches")
def get_matches(team_id: int):
    return db.get_matchesPrueba(team_id)