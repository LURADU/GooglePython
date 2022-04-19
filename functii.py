from bs4 import BeautifulSoup
import requests

r=requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link =BeautifulSoup(r.text,"html.parser")
print(link)
title=link.find_all('div',attrs={'class':'contentDiv'})
for i in title :
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            print(td_index)
            if td_index.find_all('th'):
                for th_index in td_index.find_all('th'):
                    header.append(th_index)
            for
print(header)