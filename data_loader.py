"""
Data Loader module is used to gather the data from Huawei router API.
"""
import datetime
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
    This function collects usage data from API and saves it to a JSON file.
    """
    router_api_response = requests.get(ROUTER_API_ENDPOINT)
    router_api_response.raise_for_status()
    soup = bs4.BeautifulSoup(router_api_response.content, 'lxml')
    current_month_download = int(soup.find('currentmonthdownload').get_text())
    current_month_upload = int(soup.find('currentmonthupload').get_text())
    time_stamp = datetime.datetime.now(datetime.timezone.utc)
    usage_stamp_data = {'current_month_download': current_month_download,
                        'current_month_upload': current_month_upload,
                        'time_stamp': time_stamp}
    flask_api_response = requests.put(FLASK_API_ENDPOINT, params=usage_stamp_data)
    flask_api_response.raise_for_status()



schedule.every(JOB_SCHEDULE).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
