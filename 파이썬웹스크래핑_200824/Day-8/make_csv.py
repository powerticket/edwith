import csv


def save_file(company, infos):
    file = open(f'{company}.csv', 'w', encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])
    for info in infos:
        writer.writerow(info)
    file.close()
    return
