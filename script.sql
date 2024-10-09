CREATE TABLE dept (
    deptid INT PRIMARY KEY,
    deptname VARCHAR(10) NOT NULL UNIQUE,      
    deptfullname VARCHAR(100) NOT NULL UNIQUE,
    hodname VARCHAR(20) NOT NULL
);

CREATE TABLE students (
    rollno VARCHAR(50) PRIMARY KEY,
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
    rollno VARCHAR(50),
    subjectcode VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    mark INT NOT NULL, 
    status ENUM('PASS', 'FAIL', 'AAA') NOT NULL,
    FOREIGN KEY (rollno) REFERENCES students(rollno)
);

-- Insert dummy data into dept table
INSERT INTO dept (deptid, deptname, deptfullname, hodname) VALUES 
(1,'BCA', 'Computer Application', 'MS.A.Valliyamai'),
(2,'BSC', 'Computer Science', 'I dont know'),
(3,'BCOM', 'Accounts & Finance', 'i dont Know');

-- Insert dummy data into students table
INSERT INTO students (rollno, name, age, gender, phone, fathername, mothername, address, deptid) VALUES 
('22BCA28', 'John Doe', 20, 'Male', '1234567890', 'Richard Doe', 'Jane Doe', '123 Elm St, Springfield', 1),
('22BSC03', 'Jane Smith', 19, 'Female', '0987654321', 'Mark Smith', 'Lucy Smith', '456 Oak St, Springfield', 2),
('22BCOM15', 'Emily Davis', 21, 'Female', '1112223333', 'Thomas Davis', 'Emma Davis', '789 Pine St, Springfield', 3);

-- Insert dummy data into exam table
-- Insert dummy data into exam table
INSERT INTO exam (rollno, subjectcode, subject, mark, status) VALUES 
('22BCA28', 'TAM1L', 'LANGUAGE', 85, 'PASS'),
('22BSC03', 'ENG2H', 'ENGLISH', 78, 'FAIL'),
('22BCOM15', 'MATH3', 'MATHEMATICS', 90, 'AAA');

