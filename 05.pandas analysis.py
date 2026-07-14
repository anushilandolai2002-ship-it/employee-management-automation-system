from sqlalchemy import create_engine,text
import pandas as pd
import openpyxl
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///company.db")
logging.info("create engine successfully")
try:
    df=pd.read_sql_table("employees",con=engine)
    df["annual_salary"]=df["salary"]*12
    logging.info("find annual salary successfully.")

    def category_salary(salary):
        if salary>=70000:
            return "High"
        elif salary >=40000:
            return "Medium"
        else:
            return "Low"
    df["salary_category"]=df["salary"].apply(category_salary)
    logging.info("Complete pandas analysis successfully")
except Exception as e:
    logging.error(e)

    

