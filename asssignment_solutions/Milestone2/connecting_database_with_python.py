import logging  # For logging errors
import mysql.connector  # For MySQL database connectivity
import csv  # For reading CSV files

# Establishing connection to the MySQL database
conn = mysql.connector.MySQLConnection(hostname='abc.x.y.z' (enter device hostname)
username='abc' (enter device username)
password='abcxyz'(enter device password)
port=7777 (enter port number), database='Company', password='enteryourpasword')

# Configuring logging settings
logging.basicConfig(filename='Logs/output.log', level=logging.ERROR, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Creating a cursor object to execute SQL queries
cursor = conn.cursor()

# Inserting data into the employee table if exists append data

try:
    with open('dataa/Employee_Table.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        try:
            for row in reader:
                cursor.execute("INSERT INTO employee (EMP_ID,EMP_CODE,FULL_NAME, GENDER,DATE_OF_BIRTH,DESIGNATION, JOINING_DATE, SALARY, DEPT_ID, NATIONALITY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
                conn.commit()
        except Exception as e:
            logging.error(f"An error occured while appending data in employee table: {e}")
except Exception as e:
    logging.error(f"An error occurred while executing employee table: {e}")
    
# Inserting data into the department table if exists aappend data

try:
    with open('dept.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        try:
            for row in reader:
                cursor.execute("INSERT INTO department (EMP_ID,DEPT_NAME) VALUES (%s, %s)",
                           (row[0], row[1]))
                conn.commit()
        except Exception as e:
            logging.error(f"An error occured while logging data in department table: {e}")
except Exception as e:
    logging.error(f"An error occured while executing department table: {e}")
