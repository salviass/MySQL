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
#Простий запит на вибірку######################################################
#s = User.select()

#Запит на вибірку з однією умовою##############################################
s = Carsuser.select().where(Carsuser.c.id < 3)

#Запит на вибірку з двома умовами через “and”###################################
t = text("SELECT Carsuser.username FROM Carsuser WHERE Carsuser.username BETWEEN :x and :y")
#Запит на вибірку з двома умовами через «оr»#####################################
b = text("SELECT Carsuser.username, Carsuser.id FROM Carsuser WHERE Carsuser.id = 1 OR Carsuser.id = 2")
#Запит на вибірку з використанням DISTINCT#######################################
c = text("SELECT DISTINCT Carsuser.username FROM Carsuser")
#Запит на вибірку з  умовою between…and, not between…and#########################
d= text("SELECT Carsuser.username FROM Carsuser"
        "WHERE Carsuser.id = 2 AND Carsuser.username BETWEEN :x and :y")
#Запит на вибірку з умовою in, not in############################################
e= text("SELECT Carsuser.username FROM Carsuser WHERE Carsuser.id IN (1, 2, 3, 4, 5)")
#3 запити на вибірку з умовою like з використанням різних шаблонів вибірки#######
f = text("SELECT Carsuser.username FROM Carsuser WHERE Carsuser.username LIKE(username)")
g = text("SELECT * FROM Carsuser WHERE Carsuser.id LIKE(id)")
#h = text("SELECT Carsuser.username FROM Carsuser WHERE  Carsuser.id LIKE(id>0)")
#Запит на вибірку з використанням IS NULL і IS NOT NULL##########################
a= text("SELECT * FROM Carsuser WHERE  Carsuser.username IS NOT NULL")

conn = engine.connect()

results = conn.execute(s)
print("S")
for rows in results:
    print(rows)

result = conn.execute(t, x='A', y='Z').fetchall()
print("T")
for row in result:
    print(row)

results = conn.execute(a, b, c, d, e, f, g)
print("all")
for rows in results:
    print(rows)

