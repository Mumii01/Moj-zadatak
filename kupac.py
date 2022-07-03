import sqlite3
while True:
    class Kupac:
        def __init__(self):
            self.conn = sqlite3.connect("Baza.db")
            self.cursor = self.conn.cursor()
            self.kreiranje_tabele()

        def kreiranje_tabele(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS kupac (
            id INTEGER PRIMARY KEY,
            mail VARCHAR(20),
            ime VARCHAR(20),
            drzava
            )''')

        def insert(self,Informacije):
            self.cursor.executemany('''INSERT INTO kupac (id,mail,ime,drzava) 
            VALUES (?, ?, ?, ?)''',Informacije)
            self.conn.commit()

        def read(self):
            self.cursor.execute('''SELECT * FROM kupac''')
            rows = self.cursor.fetchall()
            for x in rows:
                print(x)

        def update(self):
            ime = input('Unesite novo ime kupca: ')
            id = input('Unesite id kupca cije ime zelite promijeniti: ')
            self.cursor.execute('''UPDATE kupac SET ime = ? WHERE id = ?''',(ime,id))
            self.conn.commit()

        def delete(self):
            id = input('unesite ID kupca kojeg zelite obrisati iz tabele: ')
            self.cursor.execute('''DELETE FROM kupac WHERE id = ?''',(id,))
            self.conn.commit()

    broj_kupaca = int(input('Koliko kupaca zelite dodati u tabelu? '))
    k = Kupac()
    Informacije = []

    while broj_kupaca > 0:
        ime = str(input('unesite ime kupca: '))
        mail = str(input('unesite mail: '))
        id = int(input('unesite ID : '))
        drzava = str(input('unesite drzavu iz koje dolazi kupac: '))
        kt = (id,mail,ime,drzava)
        Informacije.append(kt)
        broj_kupaca -= 1

    k.insert(Informacije)

    user_settings = input('Izaberi opciju (read/update/delete): ').lower()
    if user_settings == 'read':
        k.read()
    elif user_settings == 'update':
        k.update()
    elif user_settings == 'delete':
        k.delete()
    else:
        break


