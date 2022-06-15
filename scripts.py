import requests
from bs4 import BeautifulSoup as BS


r = requests.get("https://mai.ru/education/studies/schedule/index.php?group=%D0%9C6%D0%9E-307%D0%91-19", verify = False)
html = BS(r.text, 'html.parser')
t = []
week = []

t = html.findAll('li', class_= 'step-item')

for data in t:
    if data.find('span', class_='text-nowrap') is not None:
        week.append(data.text)

for i in range(len(week)):

    day = week[i].replace('\n\n\n\n\n\n\n\t\t\t\t\t', '')
    #o = o.replace('\t','')
    day = day.replace('\xa0','')#начало
    day = day.replace('\t\t\t\t\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t','\n')#предмет
    day = day.replace('\n\t\t\t\t\t\t\t\t\t\t\t','\n')#лр
    day = day.replace('\n\t\t\t\t\t\t\t\t\t','')#предмет 2
    day = day.replace('\t\t\t\t\t\t\t\t\t\t\n\n\n\n\n\n','\n')#время
    day = day.replace('					','')#следующий предмет
    week[i] = day



def get_week(wnum):

    url = str('https://mai.ru/education/studies/schedule/index.php?group=%D0%9C6%D0%9E-307%D0%91-19&week=' + str(wnum))
    print(url)
    r = requests.get(url, verify=False)
    html = BS(r.text, 'html.parser')
    t = []
    week = []
    t = html.findAll('li', class_='step-item')

    for data in t:
        if data.find('span', class_='text-nowrap') is not None:
            week.append(data.text)
    print(week)
    for i in range(len(week)):

        day = week[i].replace('\n\n\n\n\n\n\n\t\t\t\t\t', '')
        # o = o.replace('\t','')
        day = day.replace('\xa0', '')  # начало
        day = day.replace('\t\t\t\t\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '\n')  # предмет
        day = day.replace('\n\t\t\t\t\t\t\t\t\t\t\t', '\n')  # лр
        day = day.replace('\n\t\t\t\t\t\t\t\t\t', '')  # предмет 2
        day = day.replace('\t\t\t\t\t\t\t\t\t\t\n\n\n\n\n\n', '\n')  # время
        day = day.replace('					', '')  # следующий предмет
        day = day.replace('\n\n\n\n', '\n\n')
        week[i] = day
        #day = ''
        
    print(week[0])
    return week
#weekres = get_week(10)
#print(weekres)
