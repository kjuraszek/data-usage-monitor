"""
Data Loader module is used to gather the data from Huawei router API.
"""
import datetime
from decimal import Decimal
import time
import configparser
import requests
import bs4
import schedule

config = configparser.ConfigParser()
config.read('data-usage-monitor.ini')

ROUTER_API_ENDPOINT = f'{config["router"]["host"]}/{config["router"]["month_statistics_endpoint"]}'
FLASK_API_ENDPOINT = (f'{config["application"]["host"]}:'
                      f'{config["application"]["flask_port"]}/'
                      f'{config["application"]["flask_endpoint"]}')
JOB_SCHEDULE = f'{config["application"]["data_loader_job_schedule"]}'


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
