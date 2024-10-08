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
