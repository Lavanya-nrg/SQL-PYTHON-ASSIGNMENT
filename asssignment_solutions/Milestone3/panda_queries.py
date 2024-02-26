from sqlalchemy import create_engine
import pandas as pd
import urllib.parse

hostname='127.0.0.1'
username='root'
password='India@123'
port=3306
database='company'

encoded_password = urllib.parse.quote_plus(password)
engine=create_engine('mysql+pymysql://'+username+':'+encoded_password+'@'+hostname+':'+str(port)+'/'+database)

conn=engine.connect()

def AvgSalaryOfEmployee():
    sql_query1=pd.read_sql_query("SELECT AVG(salary) FROM employee",conn)
    df=pd.DataFrame(sql_query1)
    print(df)


def AvgSalaryDeptWise():
    sql_query2=pd.read_sql_query("SELECT d.deptName as Department , AVG(e.salary) as avg_salary FROM department d JOIN employee e ON d.id=e.deptId GROUP BY d.deptName",conn)
    df=pd.DataFrame(sql_query2)
    print(df)

def DeptSpendMaxSalary():
    sql_query3=pd.read_sql_query("SELECT d.deptName AS department, SUM(e.salary) AS total_salary_spent FROM department d JOIN employee e ON d.id = e.deptId GROUP BY d.deptName ORDER BY total_salary_spent DESC LIMIT 1",conn)
    df=pd.DataFrame(sql_query3)
    print(df)

def DeptMaleDominated():
    sql_query4=pd.read_sql_query("SELECT d.deptName AS department, COUNT(CASE WHEN e.gender = 'Male' THEN 1 END) AS male_count FROM department d JOIN employee e ON d.id = e.deptId GROUP BY d.deptName ORDER BY male_count DESC LIMIT 1",conn)
    df=pd.DataFrame(sql_query4)
    print(df)

def MonthMaxIndianCelebrateBirthday():
    sql_query5=pd.read_sql_query("SELECT DATEPART(MONTH, birthdate) AS birth_month, COUNT(*) AS emp_count FROM employee WHERE nationality = 'Indian' GROUP BY DATEPART(MONTH, birthdate) ORDER BY emp_count DESC LIMIT 1",conn)
    df=pd.DataFrame(sql_query5)
    print(df)

def AvgSalaryDeptHeads():
    sql_query6=pd.read_sql_query("SELECT AVG(salary) AS avg_salary_department_heads FROM employee e where e.isHead='Yes'",conn)
    df=pd.DataFrame(sql_query6)
    print(df)


AvgSalaryOfEmployee()
AvgSalaryDeptWise()
DeptSpendMaxSalary()
DeptMaleDominated()
MonthMaxIndianCelebrateBirthday()
AvgSalaryDeptHeads()
