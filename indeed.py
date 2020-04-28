from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import time

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.indeed.ca/'
browser.visit(url)
browser.fill('q', 'data analyst')
button=browser.find_by_text('Find Jobs')
button.click()

title=[]
company=[]
salary=[]
location=[]
summary=[]
date=[]

for x in range(10):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    job_postings=[]
    job_postings = soup.find_all('div', class_='jobsearch-SerpJobCard')

    for job_posting in job_postings:
        title_search = job_posting.find('h2',class_='title').find('a', class_='jobtitle turnstileLink')
        title.append(title_search['title'])
        
        company_search= job_posting.find('div', class_='sjcl').find('div').find('span').text
        company.append(company_search.strip('\n'))  
        
        location_search=job_posting.find('div', class_='sjcl').find(class_= 'location accessible-contrast-color-location').text
        location.append(location_search)
        
        try:
            summary_search=job_posting.find('div', class_='summary').find('ul').text
        except AttributeError:
            summary_search="N/A"
        summary.append(summary_search.strip('\n'))
        
        try:
            salary_search=job_posting.find('div', class_='salarySnippet').find('span', class_='salary no-wrap').find('span', class_='salaryText').text
        except AttributeError:
            salary_search= "N/A"
        salary.append(salary_search.strip('\n'))
        
        date_search=job_posting.find('div', class_='jobsearch-SerpJobCard-footer').find('div', class_='jobsearch-SerpJobCard-footerActions').find('div', class_='result-link-bar-container').find('span', class_='date').text
        date.append(date_search)
        
    try: 
        browser.links.find_by_partial_href('start=').last.click()
    except:
        browser.find_by_css('.popover-x').click()   
        browser.links.find_by_partial_href('start=').last.click()

browser.quit()
           
print("Done Scrapping Indeed")
print("Job-postings scrapped:")
print(len(title))  

table= pd.DataFrame({"job_title":title,"company": company, "location":location, "salary":salary, "date": date, "summary":summary})
table=table.reset_index(drop=False)
table=table.rename(columns={"index":"id"})
table=table.set_index("id", drop=True)

########################################################################################

browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.workopolis.com/en/'
browser.visit(url)
job_search = browser.find_by_id('keyword').fill("Data Analyst")
button=browser.find_by_text('Find Jobs')
button.click()

job_title=[]
company_name=[]
job_location=[]
job_salary = []
job_summary = []
for x in range(1, 8):
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    job_postings = soup.find_all('article', class_='JobCard')
    
    
    for posting in job_postings:
        title = posting.find('h2', class_='JobCard-title')
        job_title.append(title['title'])

        company = posting.find('div', class_='JobCard-property JobCard-company').find('span').text
        company_name.append(company)

        location1 = posting.find('span', class_='JobCard-property JobCard-location').find('span').text
        location = location1.split('\xa0—\xa0')[1]
        job_location.append(location)
        try:
            salary = posting.find('span', class_='Salary').text
            job_salary.append(salary)
        except AttributeError:
            salary = posting.find('span', class_='Salary')
            job_salary.append(salary)

        summary = posting.find('div', class_='JobCard-snippet').text
        job_summary.append(summary)
    
    browser.find_by_css('.Pagination-link--next').click()

browser.quit()

print("Done Scrapping Workopolis")
print("Job-postings scrapped:")
print(len(job_title))  


workopolis=pd.DataFrame({
    'job_title':job_title,
    'company':company_name,
    'location':job_location,
    'salary':job_salary,
    'summary':job_summary})

workopolis=workopolis.reset_index(drop=False)
workopolis=workopolis.rename(columns={"index":"id"})
workopolis=workopolis.set_index("id", drop=True)

####################################################################################################

browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.glassdoor.ca/'
browser.visit(url)
browser.find_by_css('.locked-home-sign-in').click()
browser.fill('username', 'jose.dmyt@hotmail.com')
browser.fill('password', 'indeedisbetter')
browser.find_by_text('Sign In').click()
time.sleep(5)
browser.fill('sc.keyword', 'data analyst')
browser.find_by_id('HeroSearchButton').click()
browser.find_by_id('prefix__icon-close-1').click()

title=[]
company=[]
salary=[]
location=[]
summary=[]
date=[]

for x in range(4):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    job_postings=[]
    job_postings = soup.find_all('li', class_='react-job-listing')

    for job_posting in job_postings:
        title_search = job_posting.find('div',class_='jobContainer').find('a', class_='jobTitle').text
        title.append(title_search)

        company_search= job_posting.find('div', class_='jobContainer').find('div', class_='jobHeader').find('a',class_='jobInfoItem').find('div',class_='jobEmpolyerName').text
        company.append(company_search)  

        location_search=job_posting.find('div', class_='jobContainer').find('div', class_= 'empLoc').find('span',class_='loc').text
        location.append(location_search)

        try:
            salary_search=job_posting.find('div', class_='jobContainer').find('div', class_='jobFooter').find('div', class_='salaryEstimate').find('span',class_='salary').text
        except AttributeError:
            salary_search="N/A"
        salary.append(salary_search)

        try: 
            date_search=job_posting.find('div', class_='jobContainer').find('div', class_='jobFooter').find('div', class_='jobLabels').find('span',class_='jobLabel').find('span',class_='minor').text
        except AttributeError:
            date_search=job_posting.find('div', class_='jobContainer').find('div', class_='empLoc').find('div', class_='jobLabels').find('span',class_='jobLabel').find('span',class_='minor').text
        date.append(date_search)
            

    try:
        browser.find_by_css('.next').click()
    except:
        browser.find_by_css('.modal_closeIcon').click()
        browser.find_by_css('.next').click()

browser.quit()

print("Done Scrapping Glassdoor")
print("Job-postings scrapped:")
print(len(title))  

glassdoor= pd.DataFrame({"job_title":title,"company": company, "location":location, "salary":salary, "date": date})
glassdoor=glassdoor.reset_index(drop=False)
glassdoor=glassdoor.rename(columns={"index":"id"})
glassdoor=glassdoor.set_index("id", drop=True)
           

connection_string = "postgres:jose1110@localhost:5432/job_postings_db"
engine = create_engine(f'postgresql://{connection_string}')
table.to_sql(name='indeed_postings', con=engine, if_exists='append', index=True)
workopolis.to_sql(name='workopolis_postings', con=engine, if_exists='append', index=True)
glassdoor.to_sql(name='glassdoor_postings', con=engine, if_exists='append', index=True)