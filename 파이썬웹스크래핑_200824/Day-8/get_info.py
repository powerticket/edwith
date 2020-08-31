import requests
from bs4 import BeautifulSoup


def get_brand_list():
    alba_url = "http://www.alba.co.kr"
    r = requests.get(alba_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    brand_list = bs.find('div', {'id':'MainSuperBrand'}).find('ul', {'class':'goodsBox'}).find_all('li')
    info_list = {}
    for brand in brand_list:
        info_list[str(brand.find('span', {'class':'company'}).text.strip())] = str(brand.find('a')['href'])
    # print(len(company_list))
    # print(len(url_list))
    return info_list


def get_company_info(url):
    company_url = url
    r = requests.get(company_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    branch_list = bs.find('div', {'id':'NormalInfo'}).find('table')
    heads = branch_list.find('thead').find_all('th') # branch_list.find('table').find('thead').find_all('th')
    all_bodys = branch_list.find('tbody').find_all('tr')
    csv_head = []
    csv_bodys = []
    for head in heads:
        csv_head.append(head.text)
    for bodys in all_bodys:
        try:
            if not 'summaryView' in bodys.get('class', 0):
                try:
                    csv_body = []
                    csv_body.append(str(bodys.find('td').text.strip()))
                    csv_body.append(str(bodys.find('span', {'class':'company'}).text.strip()))
                    csv_body.append(str(bodys.find('span', {'class':'time'}).text.strip()))
                    csv_body.append(str(bodys.find('td', {'class':'pay'}).text.strip()))
                    csv_body.append(str(bodys.find('td', {'class':'regDate last'}).text.strip()))
                    csv_bodys.append(csv_body)
                except:
                    continue
        except:
            continue
    return csv_bodys
