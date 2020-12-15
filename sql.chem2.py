from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, \
    BOOLEAN, TIME, Text, SMALLINT, ForeignKey

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

conn = engine.connect()
