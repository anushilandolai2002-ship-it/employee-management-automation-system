from sqlalchemy import create_engine,text
import logging
import pandas as pd
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///company.db")
logging.info("create engine successfully")
try:
    with engine.begin() as conn:
        result=conn.execute(text("""SELECT COUNT(*) as total_employees,
                                 avg(salary) as average_salary,
                                 max(salary) as highest_salary,
                                 min(salary)as lowest_salary
                                 from employees"""))
        logging.info("find report successfully")
        row=result.fetchone()
        print(f"Total number of employees {row.total_employees}")       
        print(f"Total average salary of employees {row.average_salary}")       
        print(f"Total highest salary of employees {row.highest_salary}")       
        print(f"Total lowest salary of employees {row.lowest_salary}")
except Exception as e:
    logging.error(e)

try:
    with engine.begin() as conn:
        result=conn.execute(text("""SELECT department,
                                 count(*) as total_department
                                 from employees
                                 group by department"""))
        for row in result:
            print(row)
except Exception as e:
    logging.error(e)
           