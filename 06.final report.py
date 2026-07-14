from sqlalchemy import create_engine,text
import pandas as pd
import openpyxl
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///company.db")
try:
    df=pd.read_sql_table("employees",con=engine)
    logging.info("successfully connect with database.")

    df["annula_salary"]=df["salary"]*12
    logging.info("find annual salary successfully.")

    def category_salary(salary):
        if salary>=70000:
            return "High"
        elif salary>=40000:
            return "Medium"
        else:
            return "Low"
    df["salary_category"]=df["salary"].apply(category_salary)
    logging.info("create salary category successfully.")

    with engine.begin() as conn:
        total_employees=conn.execute(text("""SELECT COUNT(*) FROM employees""")).scalar()
        average_salary=conn.execute(text("""SELECT avg(salary) FROM employees""")).scalar()
        highest_salary=conn.execute(text("""SELECT max(salary) FROM employees""")).scalar()
        lowest_salary=conn.execute(text("""SELECT min(salary) FROM employees""")).scalar()

        summary=pd.DataFrame({
            "Metric":["total_salary",
                      "average_salary",
                      "highest_salary",
                      "lowest_salary"],
            "Value":[total_employees,
                     average_salary,
                     highest_salary,
                     lowest_salary]
        })
    logging.info("Data base summary create successfully.")

    department=pd.read_sql("SELECT department, COUNT(*) FROM employees group by department",engine)
    logging.info("total employees for each department get successfully.")

    with pd.ExcelWriter("final_Report.xlsx") as writer:
        df.to_excel(writer,sheet_name="Employees_data",index=False)
        summary.to_excel(writer,sheet_name="Summary",index=False)
        department.to_excel(writer,sheet_name="department_analysis",index=False)

    logging.info("Import final report successfully.")
    print("Report generated successfully.")
except Exception as e:
    logging.error(e)   
