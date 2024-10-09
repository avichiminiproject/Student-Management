import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os
# Database connection function
def connect_db():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),  # Change according to your host
        user=os.getenv('MYSQL_USERNAME'),       # Change to your MySQL user
        password="",  # Change to your MySQL password
        database=os.getenv('MYSQL_DATABASE')  # Change to your database name
)

# Search for student by rollno or phone
def search_student(rollno=None, phone=None):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    if rollno:
        cursor.execute("SELECT * FROM students WHERE rollno = %s", (rollno,))
    elif phone:
        cursor.execute("SELECT * FROM students WHERE phone = %s", (phone,))
    student = cursor.fetchone()
    db.close()
    return student

# Add new student to the database
def add_student(data):
    db = connect_db()
    cursor = db.cursor()
    query = ("INSERT INTO students (rollno, name, age, gender, phone, fathername, mothername, address, deptid) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query, (data['rollno'], data['name'], data['age'], data['gender'], data['phone'], data['fathername'], data['mothername'], data['address'], data['deptid']))
    db.commit()
    db.close()
