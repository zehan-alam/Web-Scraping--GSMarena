from bs4 import BeautifulSoup
import requests
from random import randrange

ip_addresses = []
def LoadUpProxies():
	url='https://sslproxies.org/'
	header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
	}
	response=requests.get(url,headers=header)
	soup=BeautifulSoup(response.content, 'lxml')

	for item in soup.select('div.fpl-list tr'):
		try:
			ip_addresses.append(item.select('td')[0].get_text()+':'+item.select('td')[1].get_text())
		except:
			pass

LoadUpProxies()
print(ip_addresses)
with open("ip_addresses.txt","w") as f:
    for i in ip_addresses:
        f.write(f'{i}\n')