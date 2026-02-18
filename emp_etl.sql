CREATE DATABASE HR_ETL;


USE HR_ETL;


IF OBJECT_ID('Employee_Main') IS NOT NULL
DROP TABLE Employee_Main;

CREATE TABLE Employee_Main
(
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);



IF OBJECT_ID('Employee_Staging') IS NOT NULL
DROP TABLE Employee_Staging;

CREATE TABLE Employee_Staging
(
    EmpID INT,
    EmpName VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);



INSERT INTO Employee_Main VALUES
(1,'Ravi','IT',60000),
(2,'Sita','HR',45000),
(3,'Arjun','IT',75000);


INSERT INTO Employee_Staging VALUES
(2,'Sita','HR',50000),
(4,'Meena','Finance',80000);




MERGE Employee_Main AS Target
USING Employee_Staging AS Source
ON Target.EmpID = Source.EmpID

WHEN MATCHED AND Target.Salary <> Source.Salary
THEN UPDATE SET
    Target.Salary = Source.Salary

WHEN NOT MATCHED BY TARGET
THEN INSERT (EmpID, EmpName, Department, Salary)
VALUES (Source.EmpID, Source.EmpName, Source.Department, Source.Salary);


SELECT * FROM Employee_Main;






