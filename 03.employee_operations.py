from sqlalchemy import create_engine,text
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///company.db")
def add_employee(params=None):
    try:
        with engine.begin() as conn:
            result=conn.execute(text("""INSERT INTO employees(id,name,department,salary,joining_date,email)
                        VALUES (:id,:name,:department,:salary,:joining_date,:email)"""),params or {})
            logging.info("Add employees successfully.")
            return result.rowcount
        
    except Exception as e:
        logging.error(e)
def update_salary(params=None):
    try:
        with engine.begin() as conn:
            result=conn.execute(text("""UPDATE employees 
                                     SET salary=:salary
                                     WHERE id=:id"""),params or {})
            logging.info("Update salary successfully.")
            return result.rowcount
        logging.info("Update salary successfully.")
    except Exception as e:
        logging.error(e)
def delete_employee(params=None):
    try:
        with engine.begin() as conn:
            result=conn.execute(text("""DELETE FROM employees
                                    WHERE id=:id"""),params or {})
            logging.info("DELETE employees successfully.")
            return result.rowcount
        
    except Exception as e:
        logging.error(e)
def search_employee(params=None):
    try:
        with engine.begin() as conn:
            result=conn.execute(text("""SELECT * FROM employees
                                     WHERE id=:id"""),params or {})
            logging.info("search employees successfully.")
            return result.fetchone()
        
    except Exception as e:
        logging.error(e)


        
