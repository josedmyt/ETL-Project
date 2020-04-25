-- Database: jobposting_db

-- DROP DATABASE jobposting_db;

CREATE DATABASE jobposting_db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
DROP TABLE workopolis_postings;

CREATE TABLE workopolis_postings (
  id INT PRIMARY KEY,
	job_title TEXT,
	company_name TEXT,	
	job_location TEXT,
	job_salary TEXT,
	job_summary TEXT);


