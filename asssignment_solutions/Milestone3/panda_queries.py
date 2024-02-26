from sqlalchemy import create_engine
import pandas as pd
import urllib.parse

hostname='abc.x.y.z' (enter device hostname)
username='abc' (enter device username)
password='abcxyz'(enter device password)
port=7777 (enter port number)
database='Company'

encoded_password = urllib.parse.quote_plus(password)
engine=create_engine('mysql+pymysql://'+username+':'+encoded_password+'@'+hostname+':'+str(port)+'/'+database)

conn=engine.connect()

def AvgSalaryOfEmployee():
    sql_query1=pd.read_sql_query("SELECT ROUND(AVG(E.SALARY)) AS AVGSAL FROM Employee_Table;",conn)
    df=pd.DataFrame(sql_query1)
    print(df)


def AvgSalaryDeptWise():
    sql_query2=pd.read_sql_query("SELECT E.DEPT_ID,D.DEPT_NAME,ROUND(AVG(E.SALARY),2) AS AVGSAL FROM Employee_Table AS E INNER JOIN Department_Table AS D ON E.DEPT_ID=D.DEPT_ID GROUP BY D.DEPT_ID ORDER BY E.DEPT_ID ASC;",conn)
    df=pd.DataFrame(sql_query2)
    print(df)

def DeptSpendMaxSalary():
    sql_query3=pd.read_sql_query("SELECT d.deptName AS department, SUM(e.salary) AS total_salary_spent FROM department d JOIN employee e ON d.id = e.deptId GROUP BY d.deptName ORDER BY total_salary_spent DESC LIMIT 1",conn)
    df=pd.DataFrame(sql_query3)
    print(df)

def DeptMaleDominated():
    sql_query4=pd.read_sql_query("SELECT E.DEPT_ID,D.DEPT_NAME,SUM(E.SLARY) AS DEPTSAL FROM Employee_Table AS E INNER JOIN Department_Table AS D ON D.DEPT_ID=E.DEPT_ID GROUP BY E.DEPT_ID  ORDER BY DEPTSAL LIMIT 1;",conn)
    df=pd.DataFrame(sql_query4)
    print(df)

def MonthMaxIndianCelebrateBirthday():
    sql_query5=pd.read_sql_query("SELECT EXTRACT(MONTH FROM DATE_OF_BIRTH) AS BMONTH FROM Employee_Table WHERE NATIONALITY='INDIAN' GROUP BY BMONTH ORDER BY BMONTH DESC LIMIT 1;",conn)
    df=pd.DataFrame(sql_query5)
    print(df)

def AvgSalaryDeptHeads():
    sql_query6=pd.read_sql_query("SELECT D.DEPT_HEAD_ID,ROUND(AVG(E.SALARY),2) AS AVGHEADSAL FROM E_T AS E INNER JOIN Department_Table AS D GROUP BY D.DEPT_HEAD_ID ORDER BY D.DEPT_HEAD_ID ASC;",conn)
    df=pd.DataFrame(sql_query6)
    print(df)


AvgSalaryOfEmployee()
AvgSalaryDeptWise()
DeptSpendMaxSalary()
DeptMaleDominated()
MonthMaxIndianCelebrateBirthday()
AvgSalaryDeptHeads()
