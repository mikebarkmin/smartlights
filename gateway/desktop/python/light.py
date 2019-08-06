import requests
from device import NetworkDevice
import sqlite3

db_path = "gateway.db"


class Light(NetworkDevice):

    def __init__(self, id: int, name: str, ip_address: str, port: int,
                 r: int = 0, g: int = 0, b: int = 0):
        super().__init__(ip_address, port=port)
        self.id = id
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def create_table(cls):
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS " +
            "light(id INTEGER PRIMARY KEY, " +
            "name TEXT, " +
            "ip_address TEXT, " +
            "port INTEGER, " +
            "r INTEGER, " +
            "g INTEGER, " +
            "b INTEGER)"
        )
        db.commit()
        c.close()

    @classmethod
    def get(cls, id: int):
        db = sqlite3.connect(db_path)
        c = db.cursor()
        sql = f"SELECT * FROM light WHERE id={id}"
        result = c.execute(sql).fetchone()
        c.close()

        if result:
            return Light(
                result[0],
                result[1],
                result[2],
                result[3],
                r=result[4],
                g=result[5],
                b=result[6]
            )
        else:
            return None

    @classmethod
    def all(cls):
        db = sqlite3.connect(db_path)
        c = db.cursor()
        results = c.execute(f"SELECT * FROM light").fetchall()
        db.close()

        lights = []
        for result in results:
            lights.append(
                Light(
                    result[0],
                    result[1],
                    result[2],
                    result[3],
                    r=result[4],
                    g=result[5],
                    b=result[6]
                )
            )
        return lights

    def save(self):
        db = sqlite3.connect(db_path)
        c = db.cursor()
        if self.id is None:
            # Einfügen
            sql = f"INSERT INTO light VALUES(null, '{self.name}', '{self.ip_address}', {self.port}, {self.r}, {self.g}, {self.b})"
            c.execute(sql)
        else:
            # Updaten
            c.execute(
                f"UPDATE light SET name='{self.name}', r={self.r}, g={self.g}, b={self.b} WHERE id={self.id}")
        db.commit()
        c.close()

        self.request_update()

    def delete(self):
        db = sqlite3.connect(db_path)
        c = db.cursor()
        if self.id is not None:
            c.execute(f"DELETE FROM light WHERE id={self.id}")
        db.commit()
        c.close()

    def request_update(self):
        return requests.post(f"http://{self.ip_address}:{self.port}/leds",
                             json={
                                 'r': self.r,
                                 'g': self.g,
                                 'b': self.b
                             })

    def to_dict(self):
        light = super().to_dict()
        light['name'] = self.name
        light['id'] = self.id
        light['r'] = self.r
        light['g'] = self.g
        light['b'] = self.b
        return light
