import os
import get_info
import make_csv


os.system("clear")
brand_list = get_info.get_brand_list()
for company, url in brand_list.items():
    make_csv.save_file(company, get_info.get_company_info(url))
    print(f'{company} information is scraped!')