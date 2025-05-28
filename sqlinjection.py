from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Datenbankkonfiguration
DB_CONFIG = {
    'host': '127.0.0.1',      # IP oder Hostname des MySQL/MariaDB-Servers
    'port': 3306,
    'user': 'student',
    'password': 'Steinbeis',
    'database': 'SQLInjection'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Datenbankfehler: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    daten = None
    fehlermeldung = None
    query = None

    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']

        conn = get_db_connection()
        if conn is None:
            fehlermeldung = "Fehler bei der Verbindung zur Datenbank."
        else:
            try:
                cursor = conn.cursor()
                query = f"""
                    SELECT *
                    FROM Kunden
                    WHERE vorname = "{vorname}" OR nachname = "{nachname}"
                """
                cursor.execute(query)
                daten = cursor.fetchall()
            except Error as e:
                fehlermeldung = f"Fehler bei der Abfrage: {e}"
            finally:
                cursor.close()
                conn.close()

    return render_template('index.html', daten=daten, fehlermeldung=fehlermeldung,query=query)

@app.route('/join', methods=['GET', 'POST'])
def join():
    daten = None
    fehlermeldung = None
    query = None

    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        tabelle = request.form['tabelle']

        conn = get_db_connection()
        if conn is None:
            fehlermeldung = "Fehler bei der Verbindung zur Datenbank."
        else:
            try:
                cursor = conn.cursor()
                query = f"""
                    SELECT *
                    FROM {tabelle}
                    WHERE vorname = "{vorname}" OR nachname = "{nachname}"
                """
                cursor.execute(query)
                daten = cursor.fetchall()
            except Error as e:
                fehlermeldung = f"Fehler bei der Abfrage: {e}"
            finally:
                cursor.close()
                conn.close()

    return render_template('index_join.html', daten=daten, fehlermeldung=fehlermeldung,query=query)

@app.route('/login', methods=['GET', 'POST'])
def login():
    daten = None
    fehlermeldung = None
    query = None

    if request.method == 'POST':
        vorname = request.form['vorname']
        passwort = request.form['passwort']

        conn = get_db_connection()
        if conn is None:
            fehlermeldung = "Fehler bei der Verbindung zur Datenbank."
        else:
            try:
                cursor = conn.cursor()
                query = f"""
                    SELECT vorname,passwort
                    FROM Kunden
                    JOIN Kunden_Passwoerter ON Kunden.ID = Kunden_Passwoerter.KundenID
                    WHERE vorname = "{vorname}" AND passwort = "{passwort}"
                """
                cursor.execute(query)
                daten = cursor.fetchall()
            except Error as e:
                fehlermeldung = f"Fehler bei der Abfrage: {e}"
            finally:
                cursor.close()
                conn.close()
            #app.logger.error(daten)
            if daten!=None:
                return render_template('login_erfolgreich.html', query=query)
                #print("Login erfolgreich")
            fehlermeldung = "Login fehlgeschlagen! Bitte versuche es erneut!"
            #app.logger.error("Login fehlgeschlagen")

    return render_template('login.html', fehlermeldung=fehlermeldung,query=query)



@app.route('/sicher', methods=['GET', 'POST'])
def index_sicher():
    daten = None
    fehlermeldung = None
    query = None

    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']

        conn = get_db_connection()
        if conn is None:
            fehlermeldung = "Fehler bei der Verbindung zur Datenbank."
        else:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT *
                    FROM Kunden
                    WHERE vorname = %s OR nachname = %s
                """
                cursor.execute(query, (vorname,nachname))
                daten = cursor.fetchall()
                print(daten)
            except Error as e:
                fehlermeldung = f"Fehler bei der Abfrage: {e}"
            finally:
                cursor.close()
                conn.close()

    return render_template('index.html', daten=daten, fehlermeldung=fehlermeldung,query=query)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0")