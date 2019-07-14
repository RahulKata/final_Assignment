import requests
from bs4 import BeautifulSoup
import csv
import re


base_url = "https://karki23.github.io/Weather-Data/"
source = requests.get(base_url + 'assignment.html').text
soup = BeautifulSoup(source,'lxml')

for link in soup.find_all('a', href=True):
    # print ('href: ', link['href'])
    city_name = re.sub(".html","",link['href'])
    csv_file = open(f'D:/final_Assignment/dataset/{city_name}.csv', 'w',newline='')
    csv_writer = csv.writer(csv_file)

    city = requests.get(base_url + link['href']).text
    soup1 = BeautifulSoup(city, 'lxml')
    table = soup1.find_all("tr")

    for item in table:
        list = item.text.split()
        csv_writer.writerow([list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11],list[12],list[13],list[14],list[15],list[16],list[17],list[18],list[19],list[20],list[21],list[22],list[23]])


