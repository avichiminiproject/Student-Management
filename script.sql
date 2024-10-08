CREATE TABLE dept (
    deptid INT AUTO_INCREMENT PRIMARY KEY,
    deptname VARCHAR(10) NOT NULL UNIQUE,      
    deptfullname VARCHAR(100) NOT NULL UNIQUE,
    hodname VARCHAR(20) NOT NULL
);

CREATE TABLE students (
    rollno INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    phone VARCHAR(10) NOT NULL UNIQUE,
    fathername VARCHAR(50) NOT NULL,
    mothername VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    deptid INT,
    FOREIGN KEY (deptid) REFERENCES dept(deptid)
);

CREATE TABLE exam (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rollno INT,
    subjectcode VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    mark INT NOT NULL, 
    status TEXT NOT NULL,
    FOREIGN KEY (rollno) REFERENCES students(rollno)
);

-- Insert dummy data into dept table
INSERT INTO dept (deptname, deptfullname, hodname) VALUES 
('CS', 'Computer Science', 'Dr. Alice Smith'),
('ME', 'Mechanical Engineering', 'Dr. Bob Johnson'),
('EE', 'Electrical Engineering', 'Dr. Charlie Brown');

-- Insert dummy data into students table
INSERT INTO students (rollno, name, age, gender, phone, fathername, mothername, address, deptid) VALUES 
(1, 'John Doe', 20, 'Male', '1234567890', 'Richard Doe', 'Jane Doe', '123 Elm St, Springfield', 1),
(2, 'Jane Smith', 19, 'Female', '0987654321', 'Mark Smith', 'Lucy Smith', '456 Oak St, Springfield', 2),
(3, 'Emily Davis', 21, 'Female', '1112223333', 'Thomas Davis', 'Emma Davis', '789 Pine St, Springfield', 1);

-- Insert dummy data into exam table
INSERT INTO exam (rollno, subjectcode, subject, mark, status) VALUES 
(1, 'CS101', 'Introduction to Computer Science', 85, 'Passed'),
(2, 'ME101', 'Thermodynamics', 78, 'Passed'),
(3, 'EE101', 'Circuit Analysis', 90, 'Passed');
