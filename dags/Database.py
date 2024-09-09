import psycopg2
import json

class Database:
    def __init__(self) -> None:
        with open("./config.json", "r") as config_file:
            config = json.load(config_file).get("DATABASE")
            host = config.get("HOST")
            port = config.get("PORT")
            dbname = config.get("DB")
            id = config.get("ID")
            password = config.get("PASSWORD")

            self.DB = psycopg2.connect(host=host, port=port, dbname=dbname, user=id, password=password)
            self.CURSOR = self.DB.cursor()

    def __del__(self) -> None:
        self.CURSOR.close()
        self.DB.close()
    
    def fetchall(self, sql):
        self.CURSOR.execute(sql)
        return self.CURSOR.fetchall()