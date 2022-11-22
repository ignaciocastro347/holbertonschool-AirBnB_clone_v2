-- create the database hbnb_test_db in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user with the all the permissions for the database hbnb_test_db

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- SELECT permissions for the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
