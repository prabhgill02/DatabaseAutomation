USE first_database;
CREATE TABLE IF NOT EXISTS employees(id int not null AUTO_INCREMENT, name varchar(255), PRIMARY KEY(id));
INSERT INTO employees(name) VALUES('John');