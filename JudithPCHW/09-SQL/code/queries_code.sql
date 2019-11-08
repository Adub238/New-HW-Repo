--manager_info querie:
SELECT employees.emp_no, employees.first_name, employees.last_name, dept_manager.dept_no, dept_emp.from_date, dept_emp.to_date
FROM employees
JOIN dept_manager on employees.emp_no = dept_manager.emp_no
JOIN dept_emp on employees.emp_no = dept_emp.emp_no;

--1986 querie:
SELECT emp_no, first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '1986-01-01' AND <= '1986-12-31';

--employee+salary querie
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM employees
JOIN salaries on employees.emp_no = salaries.emp_no;

--employees+departments
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no;

--HerculesB
SELECT employees.emp_no, employees.last_name, employees.first_name
FROM employees
WHERE employees.first_name='Hercules' and LEFT(employees.last_name, 1)='B';

--Sales Department
SELECT departments.dept_name, employees.emp_no, employees.last_name, employees.first_name
FROM employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name='Sales';

--sales+development
SELECT departments.dept_name, employees.emp_no, employees.last_name, employees.first_name
FROM employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name='Sales' or departments.dept_name='Development';

--last name frequency
SELECT last_name, count(*) AS bias
FROM employees
GROUP BY last_name
ORDER BY "bias" DESC;

