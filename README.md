# SQL Injection Plattform 

## Installation
1. Install Flask and Faker `pip install flask faker`
2. Install a MySQL/MariaDB database
    1. Random Data for the database can be generated using the scripts *kundendatenbank_erstellen.py* or *kundendatenbank_2tabellen.py*
4. Change the Database Credentials in sqlinjection.py to valid credentials of your MySQL/MariaDB database

## Usage
1. Change the Database Credentials to valid credentials of your MySQL/MariaDB database
2. Start the script using python3 sqlinjection.py
3. The application is served on port 5000/TCP on all interfaces.
