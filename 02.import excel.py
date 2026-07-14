import pandas as pd
from sqlalchemy import create_engine,text
import openpyxl
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
logging.info("start programming")
engine=create_engine("sqlite:///company.db")
logging.info("create engine successfully")

try:
    employees=pd.read_excel("employees.xlsx")
    logging.info("read excel file successfully")
    df=employees.to_sql("employees",con=engine,if_exists="append",index=False)
    print(employees.head())
    logging.info("save employees file successfully")
except Exception as e:
    logging.error(e)
print(employees.head())