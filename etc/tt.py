import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

count = 1
for song in songs : 
    print(str(count)+"위")
    print(song.select_one('td.info > a.title').text.strip())
    print(song.select_one('td.info > a.artist').text.strip())
    # number_tag = song.select.one("#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number")
    # title_tag = song.select.one("#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis")
    # name_tag = song.select.one("#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis")
    count = count+1

    ##print(i.select_one("").text)

##print(soup.select(#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis))
