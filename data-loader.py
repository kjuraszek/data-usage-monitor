import requests
import bs4
import schedule
import time
import json
from decimal import Decimal

API_ENDPOINT = 'http://192.168.8.1/api/monitoring/month_statistics'

def job():
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    current_dl = int(soup.find('currentmonthdownload').get_text())
    current_ul = int(soup.find('currentmonthupload').get_text())
    data_usage = float(round(Decimal((current_dl + current_ul) / (1024**3)), 3))
    print('Current usage:', data_usage)
    with open('data.json', 'w') as data_file:
        json.dump({'data_usage': data_usage}, data_file, ensure_ascii=False, indent=4)


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
