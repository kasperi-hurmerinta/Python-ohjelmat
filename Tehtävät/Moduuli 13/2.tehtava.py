## 1. Tehtävä

from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect (
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Metropolia!',
        autocommit=True
        )

app = Flask(__name__)
@app.route('/haku')
def haku():

    args = request.args
    anna_icao_koodi = str(args.get("icao"))

    sql = (f"select name from airport where ident='{anna_icao_koodi}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)