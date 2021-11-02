# library 라이브러리 # 외부 묘듈
# 유용한 프로그램을 모아 놓은 곳

# 라이브러리 설치
#pip install seaborn # = (터미널에 사용)파이썬 패키지 매니저 pip를 통해 설치되어있지 않은 라이브러리 설치

# BeautifulSoup
from urllib import request # 어떠한 웹페이지를 긁어올 수 있음
from bs4 import BeautifulSoup

content = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(content, 'html.parser')
print(soup.find('data'))

for data in soup.select("data"):
    print("시간 : ", data.select_one("tmef").getText())
    print("날씨 : ", data.select_one("wf").getText())
    print("=" * 20)
