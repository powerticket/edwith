import requests
from bs4 import BeautifulSoup


base_urls = {
    'so': 'https://stackoverflow.com/',
    'wr': 'https://weworkremotely.com/',
    'ro': 'https://remoteok.io/',
}


def get_bs(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    return bs


def bs_so():
    result = []
    bs = get_bs(base_urls.get('so')+'jobs?r=true&q=python/')
    jobs = bs.find_all('div', {'class':'grid--cell fl1'})
    for job in jobs:        
        result.append([job.h2.text.strip(), job.h3.span.text.strip(), base_urls.get('so')+job.a.get('href')])
    return result


def bs_wr():
    result = []
    bs = get_bs(base_urls.get('wr')+'remote-jobs/search?term=python/')
    jobs = bs.find('article').find_all('li')
    for job in jobs:
        if job.find('span', {'class':'title'}):
            result.append([job.find('span', {'class':'title'}).text.strip(), job.find('span', {'class':'company'}).text.strip(), base_urls.get('wr')[:-1]+job.a['href']])
    return result
    

def bs_ro():
    result = []
    bs = get_bs(base_urls.get('ro')+'remote-dev+python-jobs/')
    jobs = bs.find_all('td', {'class':'company position company_and_position'})
    for job in jobs:
        if job.h2:
            position = job.h2.text.strip()
            company = job.h3.text.strip()
            url = base_urls.get('ro')[:-1]+job.a['href']
            result.append([position, company, url])       
    return result