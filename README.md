# Employee Management Automation System

A simple employee management system built with Python, SQLAlchemy, SQLite, and Pandas. This project was created to practice database management, automation, and data analysis using real-world employee data.

## Features

- Create an employee database using SQLAlchemy
- Import employee data from an Excel file
- Perform CRUD operations (Create, Read, Update, Delete)
- Analyze employee data using Pandas
- Generate reports in Excel format
- Log application activities using Python's logging module

## Technologies Used

- Python
- SQLAlchemy
- SQLite
- Pandas
- OpenPyXL
- Logging

## Project Structure

```
01.database_create.py      # Creates the SQLite database
02.import_excel.py         # Imports employee data from Excel
03.employee_operations.py  # CRUD operations
04.pandas_analysis.py      # Data analysis using Pandas
05.report.py               # Creates summary reports
06.final_report.py         # Exports the final report

employees.xlsx             # Sample employee dataset
final_Report.xlsx          # Generated report
```

## How to Run

1. Clone this repository.
2. Install the required libraries.

```bash
pip install pandas sqlalchemy openpyxl
```

3. Run the files in the following order:

```
01.database_create.py
02.import_excel.py
03.employee_operations.py
04.pandas_analysis.py
05.report.py
06.final_report.py
```

## What I Learned

Through this project, I learned how to:

- Work with SQLAlchemy ORM
- Connect Python with SQLite
- Import and export Excel files
- Perform CRUD operations
- Analyze data using Pandas
- Organize a small Python project

## Future Improvements

- Add a command-line menu
- Create a graphical user interface
- Generate PDF reports
- Connect to MySQL or PostgreSQL
- Build a web version using Flask

## Author

**Anushilan Dolai**
I'm building practical Python and SQL projects to develop strong skills in database management, automation, and data analysis for roles such as MIS Executive, Data Operations Associate, and Data Analyst.


