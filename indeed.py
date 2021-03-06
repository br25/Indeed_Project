# -*- coding: utf-8 -*-
"""indeed.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13CZSw3awQbOHpxt3bWnwmeVr0cBU70rJ

**Indeed job Scraper**
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

"""**Setup the query and url**"""

def get_url(position, location):
  url_template = "https://www.indeed.com/jobs?q={}&l={}"
  position = position.replace(" ", "+")
  location = location.replace(" ", "+")
  url = url_template.format(position, location)
  return url

url_result = get_url("computer operator", "Houston, TX")
print(url_result)

"""*Extract the html data*"""

response = requests.get(url_result)
soup = BeautifulSoup(response.text, "lxml")
jobs = soup.find_all("div", "job_seen_beacon")
print(jobs)

"""*Prototype the model with single record*"""

job = jobs[2]
print(job.text)

job_title = job.find('h2', class_="jobTitle").text
print(job_title)

company = job.find("span" , class_="companyName").text.strip()
print(company)

job_location = job.find("div", class_="companyLocation").text.strip()
print(job_location)

rating = job.find("span", class_="ratingNumber").text
print(rating)

post_date = job.find('span', 'date').text
today = datetime.today().strftime('%d-%m-%Y')
print(f'{post_date} And Today is {today}')

summary = job.find('div', class_='job-snippet').text.strip().replace('\n', ' ')
print(summary)

# this does not exists for all jobs, so handle the exceptions
salary_tag = job.find('div', class_='attribute_snippet').text
if salary:
  salary = salary_tag.text.strip()
else:
   salary = ''

print(salary_tag)

"""*Find a job Details*"""

record = (job_title, company, job_location, rating, post_date, summary, salary_tag)
print(record)

"""*capsulated with function*"""

def get_record(job):
  """Extract job data from a single record"""
  job_title = job.find('h2', class_="jobTitle").text
  company = job.find("span" , class_="companyName").text.strip()
  job_location = job.find("div", class_="companyLocation").text.strip()
  rating = job.find("span", class_="ratingNumber").text
  post_date = job.find('span', 'date').text
  today = datetime.today().strftime('%d-%m-%Y')
  summary = job.find('div', class_='job-snippet').text.strip().replace('\n', ' ')

  # this does not exists for all jobs, so handle the exceptions
  
  salary_tag = job.find('div', class_='attribute_snippet').text
  
  if salary == true:
    salary = salary_tag.strip()
  else:
    salary = ''

  record = (job_title, company, job_location, rating, post_date, today, summary, salary_tag)
  return record


print(record)

csv_file = open('excel.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['job_title', 'company', 'job_location', 'rating', 'post_date', 'summary', 'salary'])
csv_writer.writerow([job_title, company, job_location, rating, post_date, summary, salary])

csv_file.close()