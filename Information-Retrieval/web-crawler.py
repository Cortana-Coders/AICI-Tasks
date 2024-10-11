import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

news_data = []
data_json = {
    'title': '',
    'content':'',
    'author': '',
    'url':'',
    'published_at': '',
    'scraped_at':'',
}
filename = 'scraping_result.json'

url = 'https://www.pikiran-rakyat.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'    
}

page_response = requests.get(url, headers=headers)
soup = BeautifulSoup(page_response.content, "html.parser")

if page_response.status_code == 200:
    populer = soup.find('div', class_='most__wrap')

    if populer:
        populer = populer.find_all('a')

        for item in populer:
            data_json['url'] = item.get('href')
            data_json['title'] = item.find('h2').text.strip()

            article_url = item.get('href')
            url_response = requests.get(article_url, headers=headers)
            soup2 = BeautifulSoup(url_response.content, 'html.parser')

            if url_response.status_code == 200:
                obj = soup2.find('div', class_='col-bs12-8')
                article = obj.find_next('article', class_='read__content')

                data_json['author'] = obj.find('div', class_='read__info__author').text.strip()
                data_json['published_at'] = obj.find('div', class_='read__info__date').text.replace('-','').strip()
                
                text = ''

                for strong_tag in article.find_all('strong'):
                    strong_tag.decompose()
                
                for a_tag in article.find_all('a'):
                    a_tag.decompose()
                
                for paragraph in article.find_all('p'):
                    text += paragraph.text.replace('-','').strip()
                
                data_json['content'] = text
        else:
            print(f'Request url {article_url} gagal (Status code: {url_response.status_code}) !!!')
        
        data_json['scraped_at'] = str(datetime.now().strftime("%d %B %Y, %H:%M WIB"))
        news_data.append(dict(data_json))
else:
    print(f'Request url {url} gagal (Status code: {page_response.status_code}) !!!')

# Menyimpan data berita ke dalam file JSON
if news_data:
  with open (filename, "w") as write_file:
    json.dump(news_data, write_file, indent=3)
    print(f'Data berhasil disimpan ke dalam file {filename}!')
else:
  print(f'Data tidak berhasil disimpan!')

