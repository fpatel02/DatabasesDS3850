import sqlite3

# Function to read and display all students from the StudentInfo table
def read_students():
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM StudentInfo')
    rows = cursor.fetchall()
    
    print("Student Information:")
    print("--------------------")
    for row in rows:
        print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}")
    
    conn.close()

# Main execution
if __name__ == "__main__":
    read_students()
