from bs4 import BeautifulSoup
import requests


brand_links = []
with open("brand_links.txt", "r") as f:
    for i in range(1): #change here to select how many pages to surf
        brand_links.append(f.readline()[0:-1])


i=0
phone_links= []
for link in brand_links:
    html = requests.get(link).content
    soup = BeautifulSoup(html,'lxml')
    phone_tags = soup.select('div.makers ul li a')
    for phone in phone_tags:
        link = "https://www.gsmarena.com/"+phone['href']
        phone_links.append(link)
    i=i+1
    print(f"{i} links are done")


# with open("phone_links.txt","w") as f:
#     for i in phone_links:
#         f.write(f'{i}\n')