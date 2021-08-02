import requests
from bs4 import BeautifulSoup



    counter = 0
    bank_string = []
    result = []

    header = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0)  '
                      'Gecko/20100101 Firefox/90.0'}
    link = 'https://myfin.by/currency/minsk'
    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    title = soup.find('h1').text
    head = soup.find('div', attrs={'class': 'table-responsive page_currency'})
    # создаем список банков и текущие курсы
    for x in head.find_all('tr', attrs={'class': 'tr-tb'}):
        for i in x.find_all('td'):
            result.append(i.get_text())
    # обрезаем новую строку у названия банка
    for i in range(len(result)):
        if i % 9 == 0:
            result[i] = result[i].strip()
    # делаем красивывый вовод информации
    for l in result:
        counter += 1
        bank_string.append(l)
        if counter == 9:
            l = ' '.join(bank_string)
            print(l)
            counter = 0
            bank_string = []


