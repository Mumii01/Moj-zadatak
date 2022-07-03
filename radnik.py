import sqlite3
while True:
    class Osoba:
        def __init__(self):
            self.conn = sqlite3.connect("Baza.db")
            self.cursor = self.conn.cursor()
            self.kreiranje_tabele()

        def kreiranje_tabele(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS radnik (
            id INTEGER PRIMARY KEY,
            prezime VARCHAR(20),
            ime VARCHAR(20),
            datum_rodjenja DATE
            )''')

        def insert(self,Informacije):
            self.cursor.executemany('''INSERT INTO radnik (id,prezime,ime,datum_rodjenja) 
            VALUES (?, ?, ?, ?)''',Informacije)
            self.conn.commit()

        def read(self):
            self.cursor.execute('''SELECT * FROM radnik''')
            rows = self.cursor.fetchall()
            for x in rows:
                print(x)

        def update(self):
            ime = input('Unesite novo ime: ')
            prezime = input('Unesite prezime osobe cije prezime zelite promijeniti: ')
            self.cursor.execute('''UPDATE radnik SET ime = ? WHERE prezime = ?''',(ime,prezime))
            self.conn.commit()

        def delete(self):
            id = input('unesite ID osobe koju zelite obrisati: ')
            self.cursor.execute('''DELETE FROM radnik WHERE id = ?''',(id,))
            self.conn.commit()

    broj_osoba = int(input('Koliko osoba zelite dodati u tabelu? '))
    o = Osoba()
    Informacije = []

    while broj_osoba > 0:
        ime = str(input('unesite ime osobe: '))
        prezime = str(input('unesite prezime osobe: '))
        id = int(input('unesite ID osobe: '))
        datum_rodjenja = str(input('unesite datum rodjenja osobe: '))
        kt = (id,prezime,ime,datum_rodjenja)
        Informacije.append(kt)
        broj_osoba -= 1

    o.insert(Informacije)

    user_settings = input('Izaberi opciju (read/update/delete): ').lower()
    if user_settings == 'read':
        o.read()
    elif user_settings == 'update':
        o.update()
    elif user_settings == 'delete':
        o.delete()
    else:
        break



