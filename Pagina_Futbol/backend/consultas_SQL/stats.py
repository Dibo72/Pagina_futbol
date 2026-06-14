#---------------------------ESTADISTICAS---------------------------
#importamos las librerias
import csv

import mysql.connector

#creamos una clase database para asi solo tener que llamar uan vez a la base de datos
class dataBase:
#llamamos a la bd y se la pasamos a los demas con el self
    def database_conexion(self):
    
        self.conn = mysql.connector.connect(
                host="localhost",
                user="FUTBOL",
                password="futbol",
                database="FUTBOL"
            )

        self.cursor = self.conn.cursor()
        
        def csv_load(self):
            self.cursor = self.conn.cursor()
        # Abrir CSV
        with open("equipos.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';')

            next(reader)  # salta cabecera

            for row in reader:
                self.cursor.execute("""
                    INSERT INTO equipos (id_equipo, nombre_equipo, escudo_url)
                    VALUES (:1, :2, :3)
                """, row)
                
    def get_csv(self):
        with open("equipos.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';')

            next(reader)  # Saltar cabecera

            for row in reader:
                self.cursor.execute("""
                    INSERT INTO equipos (id_equipo, nombre_equipo, escudo_url)
                    VALUES (%s, %s, %s)
                """, row)

        self.conn.commit()

        print("Datos cargados correctamente")

#hace una consulta a la bd, lo guarda en una variable y se la pasa a main, que lo manda a index
    def get_basicStats(self):
        self.database_conexion()

        self.cursor.execute("SELECT TEAM.NAME, MATCHS, GOALS_SCORED, GOALS_CONCEDED, POINTS, ID_TEAM, TEAM.LOGO" \
        " FROM CLASIFICATION JOIN TEAM ON TEAM_ID_TEAM = ID_TEAM")

        resultado = self.cursor.fetchall()
        estadisticas = []
        i = 0

        for eq in resultado:
            nombre = eq[0]
            partidos = eq[1]
            goles_favor = eq[2]
            goles_contra = eq[3]
            puntos = eq[4]
            id_equipo = eq[5]
            logo = eq[6]

            diferencia_goles = goles_favor - goles_contra
            estadisticas.append({
                "name": nombre,
                "matches": partidos,
                "goal_diference": diferencia_goles,
                "points": puntos,
                "id": id_equipo,
                "logo": logo
            })

        self.cursor.close()
        self.conn.close()

        return estadisticas

#hace una consulta a la bd, lo guarda en una variable, y devuelve un diccionario
    def get_statsTeam(self, id):
        self.database_conexion()
        sql = "SELECT * FROM TEAM WHERE ID_TEAM = %s"
        self.cursor.execute(sql, (id,))
        equipo = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        return{
            "id":equipo[0],
            "name":equipo[1],
            "points":equipo[2]
        }
    
#hace una consulta a la bd, la guarda en una variable y se lo devuelve
    def get_squad(self, id):
        self.database_conexion()
        sql = "SELECT PLAYERS FROM TEAM WHERE ID_TEAM = %s"
        self.cursor.execute(sql,(id,))

        players = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        return players
#hace una consulta a la bd, la guarda y la devuelve
    def get_matches(self, id):
        self.database_conexion()
        sql = "SELECT * FROM MATCH WHERE ID_TEAM_LOCAL = %s OR ID_TEAM_VISITOR = %s"
        self.cursor.execute(sql,(id,))

        matches = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        return matches
    
    def get_player(self, id):
        self.database_conexion()
        sql = "SELECT * FROM PLAYER WHERE ID_PLAYER = %s"
        self.cursor.execute(sql,(id,))

        player = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        return player
    
    def get_basicStatsPrueba(self):
        return [
            {
                "name": "Real Madrid",
                "matches": 38,
                "wins": 21,
                "draw": 12,
                "defeats": 5,
                "goal_diference": 45,
                "points": 92,
                "id": 1,
                "logo": "../pictures/real_madrid.png" 
            },
            {
                "name": "Barcelona",
                "matches": 38,
                "wins": 21,
                "draw": 9,
                "defeats": 7,
                "goal_diference": 38,
                "points": 85,
                "id": 2,
                "logo": "../pictures/barcelona.png" 
            },
            {
                "name": "Atletico Madrid",
                "matches": 38,
                "wins": 18,
                "draw": 12,
                "defeats": 17,
                "goal_diference": 25,
                "points": 76,
                "id": 3,
                "logo": "../pictures/atletico_de_madrid.png" 
            }
        ]
    
    def get_statsTeamPrueba(self, id):

        equipos = {
            1: {
                "name": "Real Madrid",
                "matches": 38,
                "wins": 21,
                "draw": 12,
                "defeats": 5,
                "goal_diference": 45,
                "points": 92,
                "id": 1
            },
            2: {
                "name": "Barcelona",
                "matches": 38,
                "wins": 21,
                "draw": 9,
                "defeats": 7,
                "goal_diference": 38,
                "points": 85,
                "id": 2
            },
            3: {
                "name": "Atletico Madrid",
                "matches": 38,
                "wins": 18,
                "draw": 12,
                "defeats": 17,
                "goal_diference": 25,
                "points": 76,
                "id": 3
            }
        }

        return equipos.get(id, {"error": "Equipo no encontrado"})
    
    def get_squadPrueba(self, id):
        equipos = {
            1: {
                "name": "Real Madrid",
                "jugadores": [
                    { "id":1, "nombre": "Guler" },
                    { "id":2, "nombre": "Mbappe" },
                    { "id":3, "nombre": "Vini" }
                ],
                "id": 1
            },
            2: {
                 "name": "FCBarcelona",
                "jugadores": [
                    { "id":4, "nombre": "Gordon" },
                    { "id":5, "nombre": "Lamine" },
                    { "id":6, "nombre": "Cubarsi" }
                ],
                "id": 2
            },
            3: {
                 "name": "Atletico de madrid",
                "jugadores": [
                    { "id":7, "nombre": "Julian" },
                    { "id":8, "nombre": "Barios" },
                    { "id":9, "nombre": "Oblack" }
                ],
                "id": 3
            }
        }

        return equipos.get(id, {"error": "Equipo no encontrado"})
    
    def get_playerPrueba(self, id):
        players = {
            1:{"id":1, "nombre": "Guler", "equipo": 1},
            2:{"id":2, "nombre": "Mbappe", "equipo": 1},
            3:{"id":3, "nombre": "Vini", "equipo": 1},
            4:{"id":4, "nombre": "Gordon", "equipo": 2},
            5:{"id":5, "nombre": "Lamine", "equipo": 2},
            6:{"id":6, "nombre": "Cubarsi", "equipo": 2},
            7:{"id":7, "nombre": "Julian", "equipo": 3},
            8:{"id":8, "nombre": "Barrios", "equipo": 3},
            9:{"id":9, "nombre": "Oblack", "equipo": 3}
        }

        return players.get(id)