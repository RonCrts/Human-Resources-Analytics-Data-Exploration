import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('hr.db')
c = conn.cursor()



st.title('Human Resources Analytics Data Exploration')
st.subheader('Data Information:')
st.info('The following database diagram illustrates the HR sample database:')
st.image("https://www.sqltutorial.org/wp-content/uploads/2016/04/SQL-Sample-Database-Schema.png")
st.write("""The HR sample database has seven tables:
The employees table stores the data of employees.
The jobs table stores the job data including job title and salary range.
The departments table stores department data.
The dependents table stores the employee’s dependents.
The locations table stores the location of the departments of the company.
The countries table stores the data of countries where the company is doing business.
The regions table stores the data of regions such as Asia, Europe, America, and the Middle East and Africa. The countries are grouped into regions.
The following picture shows the table names and their records.""")
st.title("SQL Queries")
st.subheader("1. Display the first name, last name, salary and department name for those employees who earn between $5,000 and $12,000.")
st.code("""
SELECT first_name, last_name, salary, department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE salary BETWEEN 5000 AND 12000;
""", language='sql')
c.execute("""
SELECT first_name, last_name, salary, department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE salary BETWEEN 5000 AND 12000;
""")
data = c.fetchall()
df = pd.DataFrame(data, columns=['first_name', 'last_name', 'salary', 'department_name'])
st.dataframe(df)
st.subheader("2.Display the maximum salary, and the minimum salary for those employees whose job title is Public Accountant.")
st.code("""SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
WHERE job_title = 'Public Accountant';
""", language='sql')
c.execute("""SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
WHERE job_title = 'Public Accountant';
""")
data = c.fetchall()
df = pd.DataFrame(data, columns=['max_salary', 'min_salary'])
st.dataframe(df)
st.subheader("3. Display the average salary for each job title.")
st.code("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title;
""", language='sql')
c.execute("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title;
""")
data = c.fetchall()
df = pd.DataFrame(data, columns=['job_title', 'average_salary'])
st.dataframe(df)
st.subheader("4. Display the average salary for each job title, and order the output by the average salary from highest to lowest.")
st.code("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title
ORDER BY average_salary DESC;
""", language='sql')
c.execute("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title
ORDER BY average_salary DESC;
""")
data = c.fetchall()
df = pd.DataFrame(data, columns=['job_title', 'average_salary'])
st.dataframe(df)
st.subheader("5. Display the average salary for each job title, and order the output by the average salary from highest to lowest. Exclude the job title whose average salary is less than $6,000.")
st.code("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title
HAVING average_salary > 6000
ORDER BY average_salary DESC;
""", language='sql')
c.execute("""
SELECT job_title, AVG(salary) AS average_salary
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
GROUP BY job_title
HAVING average_salary > 6000
ORDER BY average_salary DESC;
""")
data = c.fetchall()
df = pd.DataFrame(data, columns=['job_title', 'average_salary'])
st.dataframe(df)
