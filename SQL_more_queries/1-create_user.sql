-- This script creates the MySQL user user_0d_1 with all privileges on the MySQL server

-- Check if user_0d_1 already exists, and create the user if not
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
