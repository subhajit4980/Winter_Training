from sqlalchemy import create_engine

#! db_string = "postgresql+psycopg2://USERNAME:PASSWORD@localhost:5432/newdb"
db_string = "postgresql+psycopg2://postgres:subhajit498@localhost:5432/newdb"

db = create_engine(db_string)
# print(db)

db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
# db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

result = db.execute("SELECT * FROM films")
# print(result)
# for r in result:
#     print(r)

db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
db.execute("DELETE FROM films WHERE year='2016'")