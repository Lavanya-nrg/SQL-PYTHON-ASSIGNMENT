def execute_query_to_df(query):
    return pd.read_sql_query(query,conn)

employee_query="SELECT * FROM employee;"
department_query="SELECT * FROM department;"

employee_df=execute_query_to_df(employee_query)
department_df=execute_query_to_df(department_query)


# def AvgSalaryOfEmployee():
#     df=employee_df['salary'].mean()
#     print(df)


# def AvgSalaryDeptWise():
#     merged_df=pd.merge(employee_df,department_df,left_on='deptId',right_on='id')
#     avg_salary_dept_wise=merged_df.groupby('deptName')['salary'].mean()
#     print(avg_salary_dept_wise)

# def DeptSpendMaxSalary():
#     merged_df=pd.merge(employee_df,department_df,left_on='deptId',right_on='id')
#     dept_total_salary=merged_df.groupby('deptName')['salary'].sum()
#     dept_max_salary=dept_total_salary.idxmax()
#     print(dept_max_salary)

# def DeptMaleDominated():
#     merged_df=pd.merge(employee_df,department_df,left_on='deptId',right_on='id')
#     male_employees=merged_df[merged_df['gender']=='Male']
#     male_employee_count=male_employees.groupby('deptName').size().reset_index(name='male_count')
#     mae_dominated_dept=male_employee_count.loc[male_employee_count['male_count'].idxmax()]['deptName']
#     print(mae_dominated_dept)

# def MonthMaxIndianCelebrateBirthday():
#     indian_employees=employee_df[employee_df['nationality']=='India']
#     max_birth_month=indian_employees['birthDate'].apply(lambda x:pd.to_datetime(x).month).mode()
#     print(max_birth_month)

def AvgSalaryDeptHeads():
    avg_head_salary=employee_df[employee_df['isHead']=='Yes']['salary'].mean()
    print(avg_head_salary)


#AvgSalaryOfEmployee()
#AvgSalaryDeptWise()
#DeptSpendMaxSalary()
#DeptMaleDominated()
#MonthMaxIndianCelebrateBirthday()
AvgSalaryDeptHeads()
