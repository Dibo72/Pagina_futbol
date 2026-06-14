from fastapi import APIRouter
from consultas_SQL.stats import dataBase

#todas las rutas de este archivo empiezan con este url
router = APIRouter(prefix="/Laliga")

#creamos el objetp db para poder conectarse con el archivo que interactua con la base de datos
db = dataBase()

#rellena la url y, cuando se la llame, ejecuta la funcion definida
@router.get("/")
def get_teams():
    db.csv_load()
    return db.get_basicStatsPrueba()

@router.get("/team/{team_id}")
def get_team(team_id: int):
    return db.get_statsTeamPrueba(team_id)

@router.get("/team/{team_id}/squad")
def get_squad(team_id: int):
    return db.get_squadPrueba(team_id)