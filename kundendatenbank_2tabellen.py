import random
import faker

fake = faker.Faker("de_DE")
faker.Faker.seed(0)
random.seed(0)

# Kunden-Datensätze: ID, Vorname, Nachname, Adresse
kunden = [(1, 'Admin', 'User', 'Hauptstraße 1, 12345 Musterstadt')]

# Passwörter separat mit KundenID
passwoerter = [(1, 'AdminPass123')]

# Generiere weitere 99 Kunden
for i in range(2, 101):
    vorname = fake.first_name()
    nachname = fake.last_name()
    adresse = fake.address().replace('\n', ', ')
    password = fake.password(length=10, special_chars=False)
    
    kunden.append((i, vorname, nachname, adresse))
    passwoerter.append((i, password))

# SQL-Skript vorbereiten
sql_script = ""

# Tabelle Kunden
sql_script += """CREATE TABLE Kunden (
    ID INT PRIMARY KEY,
    Vorname VARCHAR(50),
    Nachname VARCHAR(50),
    Adresse VARCHAR(255)
);\n\n"""

# Tabelle Kunden_Passwoerter
sql_script += """CREATE TABLE Kunden_Passwoerter (
    KundenID INT,
    Passwort VARCHAR(255),
    FOREIGN KEY (KundenID) REFERENCES Kunden(ID)
);\n\n"""

# Daten in Kunden einfügen
sql_script += "INSERT INTO Kunden (ID, Vorname, Nachname, Adresse) VALUES\n"
kunden_lines = [
    f"({k[0]}, '{k[1]}', '{k[2]}', '{k[3]}')" for k in kunden
]
sql_script += ",\n".join(kunden_lines) + ";\n\n"

# Daten in Kunden_Passwoerter einfügen
sql_script += "INSERT INTO Kunden_Passwoerter (KundenID, Passwort) VALUES\n"
pw_lines = [
    f"({p[0]}, '{p[1]}')" for p in passwoerter
]
sql_script += ",\n".join(pw_lines) + ";\n"

# Speichern als SQL-Datei
with open("kunden_mit_passwoertern.sql", "w", encoding="utf-8") as f:
    f.write(sql_script)

print("SQL-Skript wurde als 'kunden_mit_passwoertern.sql' gespeichert.")
