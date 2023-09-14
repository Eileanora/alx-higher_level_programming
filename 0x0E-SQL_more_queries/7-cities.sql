-- script that creates the database hbtn_0d_usa and table cities
-- cities table:
-- id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can't be null

CREATE DATABASE IF NTO EXISTS hbtn_0d_usa
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_if INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states (id)
);
