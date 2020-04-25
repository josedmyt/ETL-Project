from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd



executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://ca.indeed.com/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

with open('./test.txt', 'w') as f:
    f.write(html)


job_search = browser.find_by_id('text-input-what').fill("Data Analyst")


button=browser.find_by_text('Find Jobs')
button.click()



sleep(10)

browser.quit