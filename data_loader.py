"""
Data Loader module is used to gather the data from Huawei router API.
"""
import datetime
from decimal import Decimal
import time
import requests
import bs4
import schedule

ROUTER_API_ENDPOINT = 'http://192.168.8.1/api/monitoring/month_statistics'
FLASK_API_ENDPOINT = 'http://127.0.0.1:5000/api/usage-stamp'
JOB_SCHEDULE = 10


def job():
    """
    A function which is scheduled within specified schedule.
    This function collects usage data from router API and makes
    a proper PUT request to insert it to the database.
    """
    router_api_response = requests.get(ROUTER_API_ENDPOINT)
    router_api_response.raise_for_status()
    soup = bs4.BeautifulSoup(router_api_response.content, 'lxml')
    current_month_download = convert_b_to_gb(int(soup.find('currentmonthdownload').get_text()))
    current_month_upload = convert_b_to_gb(int(soup.find('currentmonthupload').get_text()))
    time_stamp = datetime.datetime.now(datetime.timezone.utc)
    usage_stamp_data = {'current_month_download': current_month_download,
                        'current_month_upload': current_month_upload,
                        'time_stamp': time_stamp}
    flask_api_response = requests.put(FLASK_API_ENDPOINT, params=usage_stamp_data)
    flask_api_response.raise_for_status()
    print('Collected data:', flask_api_response.json())


def convert_b_to_gb(number):
    """
    This function converts (large) number from bytes unit to GB and returns as Decimal type.
    """
    return Decimal(number / 2 ** 30).quantize(Decimal('1.000'))


schedule.every(JOB_SCHEDULE).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
