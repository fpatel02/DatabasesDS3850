import sqlite3

# Function to create the StudentInfo table
def create_table():
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS StudentInfo (
        StudentID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Table StudentInfo created successfully in DatabaseFile.db.")

# Function to insert a new student
def insert_student(student_id, first_name, last_name):
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO StudentInfo (StudentID, FirstName, LastName)
    VALUES (?, ?, ?)
    ''', (student_id, first_name, last_name))
    conn.commit()
    conn.close()
    print(f"Inserted student: {first_name} {last_name} with ID {student_id}")

# Function to add multiple students
def add_students(students):
    for student in students:
        insert_student(student['id'], student['first_name'], student['last_name'])

# Main execution
if __name__ == "__main__":
    create_table()
    
    # List of students to add
    students_to_add = [
        {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
        {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'},
        {'id': 3, 'first_name': 'Alice', 'last_name': 'Johnson'},
        {'id': 4, 'first_name': 'Bob', 'last_name': 'Brown'}
    ]
    
    add_students(students_to_add)
