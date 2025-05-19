import sqlite3

conn = sqlite3.connect(
    "Footballers.db"
)

c = conn.cursor()

c.execute(
    """ 
        CREATE TABLE IF NOT EXISTS Footballers (
            ID integer primary key,
            name text,
            lastname text,
            age integer
        )
    """
)

c.executemany(
        'insert into Footballers (ID, name, lastname, age) values (?, ?, ?, ?)',
        [(5, 'Davit', 'Yifiani', 80),
        (4, 'Cristiano', 'Penaldo', 41),
        (3, 'Lamine', 'Yamal', 17),
        (1, 'Lionel', 'Messi', 38),
        (2, 'Karim', 'Benzema', 15)]
)



c.execute(
    """
        insert into Footballers (id, name, lastname, age) values (6, 'Jamal', 'Musiala', '19')
    """
)

c.execute(
    """
        insert into Footballers (id, name, lastname, age) values (7, 'Khvicha', 'Kvaratskhelia', '25')
    """
)
c.execute(
    """
        insert into Footballers (id, name, lastname, age) values (8, 'Kilian', 'Mbapee', '24')
    """
)
c.execute(
    """
        insert into Footballers (id, name, lastname, age) values (9, 'Arda', 'Guler', '20')
    """
)
c.execute(
    """
        insert into Footballers (id, name, lastname, age) values (10, 'Robert', 'Lewandovski', '39')
    """
)


c.execute(
    """
        update Footballers
        set name = 'Michael'
        where id = 7
    """
)

c.execute(
    """
        delete from Footballers where id = 7
    """
)

import sqlite3


c.execute('SELECT * FROM Footballers')
rows = c.fetchall()
conn.close()

for row in rows:
   print(row)