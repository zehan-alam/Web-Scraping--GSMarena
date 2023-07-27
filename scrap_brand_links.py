from bs4 import BeautifulSoup
import requests

def get_pages(link,link_list):
    html = requests.get(link).content
    soup_page = BeautifulSoup(html,"lxml")
    pages = soup_page.select("div .nav-pages a")
    for page in pages:
        link_list.append("https://www.gsmarena.com/"+page['href'])


url = "https://www.gsmarena.com/makers.php3"
html = requests.get(url).content
soup = BeautifulSoup(html,'lxml')
td_links = soup.select('tr td a')
links=[]
for anchor in td_links:
    link = "https://www.gsmarena.com/"+anchor['href']
    links.append(link)
    get_pages(link,links)
    
with open("brand_links.txt","w") as f:
    for i in links:
        f.write(f'{i}\n')