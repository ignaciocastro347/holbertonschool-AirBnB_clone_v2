-- create the database hbnb_dev_db in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user with the all the permissions for the database hbnb_dev_db

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- SELECT permissions for the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
