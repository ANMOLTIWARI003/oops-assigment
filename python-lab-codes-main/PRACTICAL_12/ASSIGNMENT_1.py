"""
Practical No: 12
Lab Assignment-1
Consider the following Employee Tables:

Table 1 - EMPLOYEE:
  EMPNO | EMP_NAME | DEPT_NAME        | SALARY | DOJ         | BRANCH
  E101  | Vivek    | R&D              | 145000 | 11-JUNE-2019| Nagpur
  E102  | Vishal   | Marketing        | 90000  | 15-MAR-2012 | Pune
  E103  | Priyal   | Product Dev.     | 120000 | 20-JULY-2018| Bangalore
  E105  | Shrushti | Product Dev.     | 80000  | 19-SEPT-2019| Nagpur
  E106  | Pranay   | Product Dev.     | 100000 | 22-OCT-2018 | Mumbai

Table 2 - DESIGNATION:
  EMPNO | EMP_NAME | DESIGNATION
  E101  | Vivek    | Project Manager
  E102  | Vishal   | Sales Manager
  E103  | Priyal   | Design Architect
  E105  | Shrushti | Software Developer
  E106  | Pranay   | Project Lead

Perform required operations using SQLite3 + Pandas.
"""

import pandas as pd
import sqlite3

# ── Create the two DataFrames ──────────────────────────────────────────────────
employee_data = {
    "EMPNO":     ["E101","E102","E103","E105","E106"],
    "EMP_NAME":  ["Vivek","Vishal","Priyal","Shrushti","Pranay"],
    "DEPT_NAME": ["R&D","Marketing","Product Development",
                  "Product Development","Product Development"],
    "SALARY":    [145000, 90000, 120000, 80000, 100000],
    "DOJ":       ["11-JUNE-2019","15-MAR-2012","20-JULY-2018",
                  "19-SEPT-2019","22-OCT-2018"],
    "BRANCH":    ["Nagpur","Pune","Bangalore","Nagpur","Mumbai"]
}

designation_data = {
    "EMPNO":       ["E101","E102","E103","E105","E106"],
    "EMP_NAME":    ["Vivek","Vishal","Priyal","Shrushti","Pranay"],
    "DESIGNATION": ["Project Manager","Sales Manager","Design Architect",
                    "Software Developer","Project Lead"]
}

emp_df  = pd.DataFrame(employee_data)
des_df  = pd.DataFrame(designation_data)

# ── Load into in-memory SQLite database ───────────────────────────────────────
conn = sqlite3.connect(":memory:")
emp_df.to_sql("EMPLOYEE",    conn, index=False, if_exists="replace")
des_df.to_sql("DESIGNATION", conn, index=False, if_exists="replace")

def run_query(title, sql):
    print("=" * 68)
    print(f" {title}")
    print("=" * 68)
    result = pd.read_sql_query(sql, conn)
    print(result.to_string(index=False))
    print()
    return result

# ──────────────────────────────────────────────────────────────────────────────
# 1. Display all employees
# ──────────────────────────────────────────────────────────────────────────────
run_query("ALL EMPLOYEES",
    "SELECT * FROM EMPLOYEE")

# ──────────────────────────────────────────────────────────────────────────────
# 2. Display all designations
# ──────────────────────────────────────────────────────────────────────────────
run_query("ALL DESIGNATIONS",
    "SELECT * FROM DESIGNATION")

# ──────────────────────────────────────────────────────────────────────────────
# 3. Employee with highest salary
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEE WITH HIGHEST SALARY",
    "SELECT EMPNO, EMP_NAME, DEPT_NAME, SALARY FROM EMPLOYEE "
    "WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEE)")

# ──────────────────────────────────────────────────────────────────────────────
# 4. Employee with lowest salary
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEE WITH LOWEST SALARY",
    "SELECT EMPNO, EMP_NAME, DEPT_NAME, SALARY FROM EMPLOYEE "
    "WHERE SALARY = (SELECT MIN(SALARY) FROM EMPLOYEE)")

# ──────────────────────────────────────────────────────────────────────────────
# 5. Employees from Nagpur branch
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEES FROM NAGPUR BRANCH",
    "SELECT * FROM EMPLOYEE WHERE BRANCH = 'Nagpur'")

# ──────────────────────────────────────────────────────────────────────────────
# 6. Employees in Product Development department
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEES IN PRODUCT DEVELOPMENT",
    "SELECT * FROM EMPLOYEE WHERE DEPT_NAME = 'Product Development'")

# ──────────────────────────────────────────────────────────────────────────────
# 7. Average salary of all employees
# ──────────────────────────────────────────────────────────────────────────────
run_query("AVERAGE SALARY",
    "SELECT ROUND(AVG(SALARY),2) AS AVG_SALARY FROM EMPLOYEE")

# ──────────────────────────────────────────────────────────────────────────────
# 8. Employees with salary > 100000
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEES WITH SALARY > 100000",
    "SELECT EMPNO, EMP_NAME, SALARY FROM EMPLOYEE WHERE SALARY > 100000")

# ──────────────────────────────────────────────────────────────────────────────
# 9. JOIN: Employee details with their Designation
# ──────────────────────────────────────────────────────────────────────────────
run_query("EMPLOYEE DETAILS WITH DESIGNATION (JOIN)",
    """SELECT E.EMPNO, E.EMP_NAME, D.DESIGNATION, E.DEPT_NAME,
              E.SALARY, E.BRANCH
       FROM EMPLOYEE E
       JOIN DESIGNATION D ON E.EMPNO = D.EMPNO
       ORDER BY E.SALARY DESC""")

# ──────────────────────────────────────────────────────────────────────────────
# 10. Count employees per department
# ──────────────────────────────────────────────────────────────────────────────
run_query("COUNT OF EMPLOYEES PER DEPARTMENT",
    """SELECT DEPT_NAME, COUNT(*) AS TOTAL_EMPLOYEES,
              SUM(SALARY) AS TOTAL_SALARY, ROUND(AVG(SALARY),2) AS AVG_SALARY
       FROM EMPLOYEE
       GROUP BY DEPT_NAME
       ORDER BY TOTAL_EMPLOYEES DESC""")

conn.close()
print("All queries executed successfully.")