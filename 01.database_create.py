from sqlalchemy import create_engine,text
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///company.db")
logging.info("create database successfully!")
try:
    with engine.begin() as conn:
        conn.execute(text("""CREATE TABLE IF NOT EXISTS employees(
                          id INTEGER PRIMARY KEY ,
                          name TEXT,
                          department TEXT,
                          salary INTEGER,
                          joining_date TEXT,
                          email TEXT)"""))
        logging.info("Successfully create employees table")
except Exception as e:
    logging.error(e)

