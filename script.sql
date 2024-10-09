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
    deptname VARCHAR(10),
    FOREIGN KEY (deptname) REFERENCES dept(deptname)
);

CREATE TABLE exam (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rollno VARCHAR(50),
    subjectcode VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    mark INT NOT NULL, 
    status ENUM('PASS', 'FAIL', 'AAA'),
    FOREIGN KEY (rollno) REFERENCES students(rollno)
);

DELIMITER $$

CREATE TRIGGER update_exam_status
AFTER INSERT ON exam
FOR EACH ROW
BEGIN
    IF NEW.mark IS NULL THEN
        SET NEW.status = 'AAA';
    ELSEIF NEW.mark >= 40 THEN
        SET NEW.status = 'PASS';
    ELSE
        SET NEW.status = 'FAIL';
    END IF;
END $$

DELIMITER ;


-- Insert dummy data into dept table
INSERT INTO dept (deptid, deptname, deptfullname, hodname) VALUES 
(1,'BCA', 'Computer Application', 'MS.A.Valliyamai'),
(2,'BSC', 'Computer Science', 'I dont know'),
(3,'BCOM', 'Accounts & Finance', 'i dont Know');

-- Insert dummy data into students table
INSERT INTO students (rollno, name, age, gender, phone, fathername, mothername, address, deptname) VALUES 
('22BCA28', 'John Doe', 20, 'Male', '1234567890', 'Richard Doe', 'Jane Doe', '123 Elm St, Springfield', 'Computer Application'),
('22BSC03', 'Jane Smith', 19, 'Female', '0987654321', 'Mark Smith', 'Lucy Smith', '456 Oak St, Springfield', 'Computer Science'),
('22BCOM15', 'Emily Davis', 21, 'Female', '1112223333', 'Thomas Davis', 'Emma Davis', '789 Pine St, Springfield', 'Accounts & Finance');


-- Insert dummy data into exam table
INSERT INTO exam (rollno, subjectcode, subject, mark) VALUES 
('22BCA28', 'TAM1L', 'LANGUAGE', 85),
('22BSC03', 'ENG2H', 'ENGLISH', 78),
('22BCOM15', 'MATH3', 'MATHEMATICS', 90);

