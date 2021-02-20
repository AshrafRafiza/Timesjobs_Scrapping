from bs4 import BeautifulSoup
import requests
import csv

# scrapping jobs that related to python
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# open and write csv file
file = open('posts/timesjobs.csv', 'w')
writer = csv.writer(file)

# write header rows
writer.writerow(['Published Date','Company Name', 'Skills', 'More Info'])

# find specific details in each job cards in the website
for job in jobs:
	# there will be lot of \r, \n and \t after scrapping the text which need to be remove hence a lot of '.replace()'
    published_date = job.find('span', class_ = 'sim-posted').span.text.replace('\r','').replace('\n','').replace('\t','')
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').strip().replace('\r','').replace('\n','').replace('\t','')
    # there will be multiple skills which will be seperated by '-'
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').strip().replace(',','-') 
    more_info = job.header.h2.a['href']

    # write all the texts into the csv file
    writer.writerow([published_date, company_name, skills, more_info])

#close the csv file
file.close()
