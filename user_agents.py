import requests
from lxml import html
import json

BASE_URL = "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
XPATH_USER_AGENTS = '//td[@class="useragent"]/a/text()'
user_agents_list = []

for pg_number in range(2, 10):
    url = BASE_URL + str(pg_number)
    page = requests.get(url,headers=HEADERS)
    doc = html.fromstring(page.content)
    user_agents_list += [ua for ua in doc.xpath(XPATH_USER_AGENTS)]

with open('user-agents.txt', 'w') as filehandle:  
    # store the data as binary data stream
    json.dump(user_agents_list, filehandle)
