import schedule
import time
import pytz
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine, String, Column, Integer, DateTime

engine = create_engine("sqlite:///db.db")

class Base(DeclarativeBase):
    pass

class Facts(Base):
    __tablename__ = "facts"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    last_used = Column(DateTime)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def send_fact():
    pass

schedule.every().day.at("12:28", "Europe/Warsaw").do(send_fact)

while True:
    schedule.run_pending()
    time.sleep(1)
