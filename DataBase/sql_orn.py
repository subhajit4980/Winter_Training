from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:subhajit498@localhost:5432/FLIM"
db = create_engine(db_string)
base = declarative_base()


class Flim(base):
    __tablename__ = "flimORM"
    title = Column(String, primary_key=True)
    director = Column(String, nullable=False)
    year = Column(String, nullable=False)


Session = sessionmaker(db)
sess = Session()
# base.metadata.create_all(db)

#
doctor_strange = Flim(
    title="doctor strange multiverse1",
    director="Director",
    year="2021"
)
# sess.add(doctor_strange)
# sess.commit()

Flims = sess.query(Flim)

for flim in Flims:
    print(flim.title)

#
# doctor_strange.title="some flim3"
# sess.commit()

user1 = sess.query(Flim).filter_by(title=doctor_strange.title).first()
sess.delete(user1)
#
# sess.delete(doctor_strange)
sess.commit()

#
