import sqlite3
from student import Student

class Student_Exercise_Reports():

    #  """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/caroline/workspace/python/Tracking_Student_Exercises/studentexercises.db"

    # It's time to create your Student instances!!! The sqlite3 package has a row_factory property on the connection object where you can specify the instructions for the conversion of row of data -> Student instance with your own function. The function assigned to the row_factory property must take two arguments - the cursor, and the current row of data. It must return something. In your case, it will return a new instance of student.(Chapter Documentation, NSS)

    # Then assign this function to the row_factory method of the database connection.

    # def create_student(self, cursor, row):
    #     return Student(row[1], row [2], row[3], row[5])

    # COMMENTED OUT ABOVE FUNCTION:  You can delete the create_student() function and define it as a lambda instead. LAMBDA = ANONYMOUS FUNCTION IN PYTHON (CHAPTER DOC, NSS)

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            # takes the list of tuples and passes each row in and creates a student 
            # conn.row_factory = self.create_student

            # USING LAMBDA IN PLACE OF ABOVE STATEMENT
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            select s.student_id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.cohort_id
            order by s.cohort_id
            """)

            # When you instruct the sqlite3 package to fetchall(), it takes your SQL string and walks over to the database and executes it. It then takes all of the rows that the database generates, and creates a tuple out of each one. It then puts all of those tuples into a list. (Chapter Documentation, NSS)

            # TUPLE is a collection which is ordered and unchangeable. Allows duplicate members. Parenthesis. (W3 Schools)

            # LIST is a collection which is ordered and changeable. Allows duplicate members. Brackets. (W3 Schools)

            all_students = db_cursor.fetchall()

            # for student in all_students:

                # Since a tuple is simply an immutable list, you can use square-bracket notation to extract individual items out of it. Displaying a tuple to the terminal as output is not good UX. Use the following code to just display the first name (second column), last name (third column), and cohort name (sixth column). (Chapter Documentation, NSS)

                # The index numbers correspond to the position of values in the SQL string above. (Self Notes)

                # print(f'{student[1]} {student[2]} is in {student[5]}')
                # Changed print statement after def create_student was created
                # print(f'{student.first_name} {student.last_name} is in {student.cohort}')

                # COMMENT OUT ABOVE PRINT STATEMENT AND REPLACE WITH... 

            for student in all_students:
                print(student)

                # SINCE ADDING A __repr__() METHOD TO STUDENT.PY

    
reports = Student_Exercise_Reports()
reports.all_students()