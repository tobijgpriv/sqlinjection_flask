import random
import faker

fake = faker.Faker("de_DE")
faker.Faker.seed(0)
random.seed(0)

entries = [(1, 'Admin', 'User', 'AdminPass123', 'Hauptstraße 1, 12345 Musterstadt')]

for i in range(2, 101):
    vorname = fake.first_name()
    nachname = fake.last_name()
    password = fake.password(length=10, special_chars=False)
    adresse = fake.address().replace('\n', ', ')
    entries.append((i, vorname, nachname, password, adresse))

sql_script = "CREATE TABLE Kunden (\n" \
             "    ID INT PRIMARY KEY,\n" \
             "    Vorname VARCHAR(50),\n" \
             "    Nachname VARCHAR(50),\n" \
             "    Passwort VARCHAR(255),\n" \
             "    Adresse VARCHAR(255)\n" \
             ");\n\n"

sql_script += "INSERT INTO Kunden (ID, Vorname, Nachname, Passwort, Adresse) VALUES\n"
value_lines = []

for entry in entries:
    values = f"({entry[0]}, '{entry[1]}', '{entry[2]}', '{entry[3]}', '{entry[4]}')"
    value_lines.append(values)

sql_script += ",\n".join(value_lines) + ";\n"

# Ausgabe oder speichern
with open("kunden.sql", "w", encoding="utf-8") as f:
    f.write(sql_script)

print("SQL-Script wurde als 'kunden.sql' gespeichert.")
