-- This script prepares a MySQL server for the project.

-- Create a new database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- Grant select privileges on the performance_schema database to the new user
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
