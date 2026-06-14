#---------------------------MAIN---------------------------
#importamos las librerias, tambien definen como es la estructura del proyecto de python
from fastapi import FastAPI
from router import teams, players, matches

#creamos un objeto que gestiona todo
app = FastAPI()

#hacemos que los routers existan en el programa
app.include_router(teams.router)
app.include_router(players.router)
app.include_router(matches.router)