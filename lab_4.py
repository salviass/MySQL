from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, \
    BOOLEAN, TIME, Text, SMALLINT, ForeignKey

from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:mysql@localhost/grechko", echo=True)
meta = MetaData()

Car = Table(
    'car', meta,
    Column('id', Integer, primary_key=True),
    Column('text', String(255), nullable=False),
)

Cardescription = Table(
    'cardescription', meta,
    Column('id', Integer, primary_key=True),
    Column('text', String(32), nullable=False),

)

Carsuser = Table(
    'carsuser', meta,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('username', String(80)),
)
meta.create_all(engine)

#Запит з використанням LEFT #########################################################################
a = text("SELECT DISTINCT Car.text, Cardescription.text FROM Car LEFT JOIN Cardescription ON Car.text = Cardescription.text")
#Запит з використанням RIGHT ########################################################################
b = text("SELECT DISTINCT Car.text, Cardescription.text FROM Car RIGHT JOIN Cardescription ON Car.text = Cardescription.text")
# Запит з використанням функцій REPLACE #############################################################
c = text("SELECT  id, REPLACE(username, 'z', '-') AS username FROM Carsuser ")
#Запит з використанням функцій LTRIM, RTRIM, TRIM ###################################################
d= text("SELECT TRIM(' Andrew ') AS Users ")
#Запит з використанням функцій LOWER, UPPER #########################################################
e = text("SELECT UPPER(' Andrew ') AS Users ")
#Запит з використанням функцій REPEAT ###############################################################
f= text("SELECT username, REPEAT(id, 4) FROM Carsuser ")
#Запит з використанням функцій REVERSE ##############################################################
g = text("SELECT email, REVERSE(email) AS email FROM Carsuser ")
#Запит з використанням функцій CONCAT ###############################################################
h = text("SELECT username, CONCAT('!!!', username, '???') AS username FROM Carsuser ")
#Запит з використанням функцій LENGHT ###############################################################
j = text("SELECT *, LENGTH(username) as length FROM Carsuser ")

conn = engine.connect()

result = conn.execute(a)
for row in result:
    print(row[0])

result = conn.execute(b)
for row in result:
    print(row[0])

result = conn.execute(c)
for row in result:
    print(row[0])

result = conn.execute(d)
for row in result:
    print(row[0])

result = conn.execute(e)
for row in result:
    print(row[0])

result = conn.execute(f)
for row in result:
    print(row[0])

result = conn.execute(g)
for row in result:
    print(row[0])

result = conn.execute(h)
for row in result:
    print(row[0])

result = conn.execute(j)
for row in result:
    print(row[0])
