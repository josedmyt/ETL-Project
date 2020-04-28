CREATE TABLE indeed_postings (
	id INT PRIMARY KEY,
	job_title TEXT,
	company TEXT,
	location TEXT,
	salary TEXT,
	date TEXT,
	summary TEXT);
	
CREATE TABLE workopolis_postings (
    id INT PRIMARY KEY,
	job_title TEXT,
	company_name TEXT,	
	job_location TEXT,
	job_salary TEXT,
	job_summary TEXT);

CREATE TABLE glassdoor_postings (
	id INT PRIMARY KEY,
	job_title TEXT,
	company TEXT,
	location TEXT,
	salary TEXT,
	date TEXT);
	
DROP TABLE indeed_postings;
DROP TABLE workopolis_postings;	
DROP TABLE glassdoor_postings;

SELECT * FROM indeed_postings;
SELECT * FROM workopolis_postings
SELECT * FROM glassdoor_postings;