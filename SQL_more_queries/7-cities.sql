-- This script creates the database hbtn_0d_usa and the table cities with required constraints

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT si_state FOREIGN KEY (state_id) REFERENCES states(id)
);
