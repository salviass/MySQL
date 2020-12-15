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

Cardescription= Table(
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

#Запит з функцією min або max###############################################################
#Запит на вибірку з використанням агрегатної функції і виведенням ще декількох полів########
a = text("SELECT MAX(Carsuser.id) AS maximum FROM Carsuser")
#Запит з функцією sum або avg###############################################################
b = text("SELECT SUM(Carsuser.id) FROM Carsuser")
#Запит з функцією count#####################################################################
c = text("SELECT count(*) FROM Carsuser")
#Запит на вибірку з використанням агрегатної функції і умовою на вибірку поля###############
d = text("SELECT MIN(Carsuser.id) FROM Carsuser WHERE Carsuser.username IS NOT NULL")
#Запит на вибірку з використанням агрегатної функції і умовою на агрегатну функцію##########
e = text("SELECT MIN(Carsuser.id) FROM Carsuser WHERE Carsuser.id = 1 OR Carsuser.id = 2")
#Запит на вибірку з використанням агрегатної функції, умовою на агрегатну функцію, умовою на
# вибірку поля з сортуванням даних.#########################################################
t = text("SELECT MIN(Carsuser.id) FROM Carsuser WHERE Carsuser.id = 1 OR Carsuser.id = 2 ORDER BY Carsuser.id")

conn = engine.connect()

result = conn.execute(t)
for row in result:
    print(row[0])

result = conn.execute(a, b, c, d, e)
for row in result:
    print(row[0])
