from bs4 import BeautifulSoup
import requests
import time

print('Type a skill you do not want on the listing')
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill}')


def find_jobs():
    output = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(output, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 18
        print(f'Waiting 30 minutes...')
        time.sleep(time_wait * 100)
