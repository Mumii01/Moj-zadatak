import sqlite3
while True:
    class Masina:
        def __init__(self):
            self.conn = sqlite3.connect("Baza.db")
            self.cursor = self.conn.cursor()
            self.kreiranje_tabele()

        def kreiranje_tabele(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS masine (
            proizvodjac VARCHAR(30),
            naziv VARCHAR(20),
            broj_osa INTEGER
            )''')

        def insert(self,Informacije):
            self.cursor.executemany('''INSERT INTO masine (proizvodjac,naziv,broj_osa) 
            VALUES (?, ?, ?)''',Informacije)
            self.conn.commit()

        def read(self):
            self.cursor.execute('''SELECT * FROM masine''')
            rows = self.cursor.fetchall()
            for x in rows:
                print(x)

        def update(self):
            broj_osa = input('Unesite novi broj osa: ')
            naziv = input('Unesite naziv masine ciji broj radnih osa zelite promijeniti: ')
            self.cursor.execute('''UPDATE masine SET broj_osa = ? WHERE naziv = ?''',(broj_osa,naziv))
            self.conn.commit()

        def delete(self):
            naziv = input('unesite naziv masine koju zelite obrisati: ')
            self.cursor.execute('''DELETE FROM radnik WHERE naziv = ?''',(naziv,))
            self.conn.commit()

    broj_masina = int(input('Koliko masina zelite dodati u tabelu? '))
    m = Masina()
    Informacije = []

    while broj_masina > 0:
        proizvodjac = str(input('unesite proizvodjaca masine: '))
        naziv = str(input('unesite naziv masine: '))
        broj_osa = int(input('unesite broj osa masine: '))
        ty = (proizvodjac,naziv,broj_osa)
        Informacije.append(ty)
        broj_masina -= 1

    m.insert(Informacije)

    user_settings = input('Izaberi opciju (read/update/delete): ').lower()
    if user_settings == 'read':
        m.read()
    elif user_settings == 'update':
        m.update()
    elif user_settings == 'delete':
        m.delete()
    else:
        break

