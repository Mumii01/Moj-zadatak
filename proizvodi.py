import sqlite3
while True:
    class Proizvod:
        def __init__(self):
            self.conn = sqlite3.connect("Baza.db")
            self.cursor = self.conn.cursor()
            self.kreiranje_tabele()

        def kreiranje_tabele(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS proizvodi (
            sifra_proizvoda INTEGER PRIMARY KEY,
            kolicina INTEGER,
            naziv VARCHAR(20),
            cijena INTEGER
            )''')

        def insert(self,Informacije):
            self.cursor.executemany('''INSERT INTO proizvodi (sifra_proizvoda,kolicina,naziv,cijena) 
            VALUES (?, ?, ?, ?)''',Informacije)
            self.conn.commit()

        def read(self):
            self.cursor.execute('''SELECT * FROM proizvodi''')
            rows = self.cursor.fetchall()
            for x in rows:
                print(x)

        def update(self):
            kolicina = input('Unesite novu kolicinu: ')
            sifra_proizvoda = input('Unesite sifru proizvoda ciju kolicinu zelite promijeniti: ')
            self.cursor.execute('''UPDATE proizvodi SET kolicina = ? WHERE sifra_proizvoda = ?''',
                                (kolicina,sifra_proizvoda))
            self.conn.commit()

        def delete(self):
            sifra_proizvoda = input('unesite ID osobe koju zelite obrisati: ')
            self.cursor.execute('''DELETE FROM proizvodi WHERE sifra_proizvoda = ?''',(sifra_proizvoda,))
            self.conn.commit()

    broj_proizvoda = int(input('Koliko proizvoda zelite dodati u tabelu? '))
    p = Proizvod()
    Informacije = []

    while broj_proizvoda > 0:
        naziv = str(input('unesite naziv proizvoda: '))
        kolicina = int(input('unesite kolicinu tog proizvoda: '))
        sifra_proizvoda = int(input('unesite sifru proizvoda: '))
        cijena = int(input('unesite cijenu proizvoda: '))
        sve = (sifra_proizvoda,kolicina,naziv,cijena)
        Informacije.append(sve)
        broj_proizvoda -= 1

    p.insert(Informacije)

    user_settings = input('Izaberi opciju (read/update/delete): ').lower()
    if user_settings == 'read':
        p.read()
    elif user_settings == 'update':
        p.update()
    elif user_settings == 'delete':
        p.delete()
    else:
        break


