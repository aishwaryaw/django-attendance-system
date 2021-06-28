# django-attendance-system

Built a simple employee attendance system with Django framework and PostgreSQL database system in the backend and HTML, CSS with Bootstrap4, JavaScript in the frontend where each employee's today's attendance can be filled in one go if not already done, if already filled then can be viewed, previous attendance details can also be viewed with date range filtering functionality.
Employee details can be added, updated and deleted with the help of validation forms.
Employees data can be filtered with the help of email searching functionality and departments selection.

Below are the functionalities for each individual page:
1. All attendance dashboard : On this page, all employees listing will be displayed. For each employee, edit and delete functionalities are provided. Along with this, employee attendance details will be displayed after clicking on employee name. Employees data can be filtered with email and department searching.
2. View today's attendance : On this page, today's attendance for all the employees will be displayed if attendance details are already filled for that specific day. Otherwise, edit today's attendance page will be displayed where employee attendance details can be filled for all employees.
3. Edit today's attendance : Here, each employee's attendance status can be updated in one go and it's mandatory to update attendance details of all the listed employees else validation error will be displayed.
4. Add new employee : Here, new employee record can be added. Validations are performed on all the form fields before saving.the details into database. Also, one more feature is added here. If attendance details are already filled on that particular date then along with employee creation form one more form will be displayed which is attendance form having only one field in it i.e. is present field. Validations are performed on this form also. If today's attendance is not filled already,then attendance form will not be displayed in employee creation.
5. Update existing employee details : Here, existing employee details can be updated after performing all the form field validations.
6. Delete employee : Employee record can be deleted using this functionality.
7. View individual employee attendance details : Here, attendance details of an individual employee can be viewed for all the previous filled dates. Also, filtering can be done on this data using provided date range searching.
