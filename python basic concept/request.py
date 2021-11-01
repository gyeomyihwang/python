# requests
import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.naver.com/") # get을 통해 html 파일을 모두 가져옴(get)
print(res.content) # res 안의 content를 가져와서 print.

soup = BeautifulSoup(res.content, 'html.parser') 
print(soup.find('title')) # [<title>NAVER</title>]
print(soup.find('title').getText()) # NAVER
print(soup.prettify()) # indention 과 함께 정렬해서 soup 표시