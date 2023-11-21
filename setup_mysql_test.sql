-- This script prepares a MySQL Test server for the project.

-- Create a new test database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new test user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the new test database to the new test user
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';

-- Grant select privileges on the performance_schema database to the new test user
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
