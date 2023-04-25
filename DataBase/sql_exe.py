from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

#! db_string = "postgresql+psycopg2://USERNAME:PASSWORD@localhost:5432/batch2db"
db_string = "postgresql+psycopg2://postgres:PASSWORD@localhost:5432/newdb"

db = create_engine(db_string)

meta = MetaData(db)

#* Create a table
films_table = Table(
    'films_exp', 
    meta,
    Column('title', String),
    Column('director', String),
    Column('year', String)
)

# with db.connect() as conn:

#     #* Create
#     films_table.create()

#     #* Insert data
#     insert_statement = films_table.insert().values(
#         title="Doctor Strange",
#         director="Rohit Shetty",
#         year="2016"
#     )
#     conn.execute(insert_statement)

    #* Read