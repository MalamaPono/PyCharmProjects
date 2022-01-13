# This code is from Web Scraping with Beautiful Soup
# from Free Code Camp on Youtube. We can use beautiful soup to pretty
# much parse any html webpage

from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skills = input('Enter the skills you are unfamiliar with separated by spaces > ').split()
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

def find_jobs(jobs_found):
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            skills = job.find('span',class_='srp-skills').text.replace(' ','').strip()

            allFamiliar = True

            for unfamiliar_skill in unfamiliar_skills:
                if unfamiliar_skill in skills:
                    allFamiliar = False

            if allFamiliar:
                with open(f'posts/{index}.txt','w') as file:
                    company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','').strip()
                    link = job.header.h2.a['href']
                    file.write(f'Company Name: {company_name } \n')
                    file.write(f'Required Skills: {skills} \n')
                    file.write(f'Link :{link}')
                    jobs_found += 1

    return jobs_found

jobs_found = 0
max_jobs = 20
if __name__ == '__main__':
    while jobs_found < max_jobs:
        jobs_found = find_jobs(jobs_found)
        # time.sleep(5)

print('Finished finding amount of jobs wanted')

# if you don't scroll down on page I am pretty sure this
# code simply keeps returning the same jobs on first page everytime.
# To fix this we could grab new html by loading more jobs
# after calling the function each time.