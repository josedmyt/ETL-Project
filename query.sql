CREATE TABLE indeed_postings (
	job_title TEXT,
	company TEXT,
	location TEXT,
	salary TEXT,
	date TEXT,
	summary TEXT,
	website TEXT);
	
CREATE TABLE workopolis_postings (
    id INT PRIMARY KEY,
	job_title TEXT,
	company TEXT,	
	location TEXT,
	salary TEXT,
	summary TEXT,
	website TEXT);

CREATE TABLE glassdoor_postings (
	id INT PRIMARY KEY,
	job_title TEXT,
	company TEXT,
	location TEXT,
	salary TEXT,
	date TEXT, 
	website TEXT);
	
DROP TABLE indeed_postings;
DROP TABLE workopolis_postings;	
DROP TABLE glassdoor_postings;

SELECT * FROM indeed_postings;
SELECT * FROM workopolis_postings;
SELECT * FROM glassdoor_postings;

SELECT job_title, company  FROM workopolis_postings
WHERE company='Scotiabank';

SELECT * FROM workopolis_postings UNION ALL SELECT * FROM glassdoor_postings 

