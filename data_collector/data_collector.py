"""
Data Collector module is used to gather the data from Huawei router API.
"""
import datetime
import logging
import logging.config
from decimal import Decimal
import warnings
import os
import time
import configparser
from urllib3.util.retry import Retry
from urllib3.exceptions import MaxRetryError
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError, HTTPError  # pylint: disable=W0622
import bs4
import schedule


_CONFIG_FILE_NAME = 'data-usage-monitor.ini'

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), _CONFIG_FILE_NAME))
logger = logging.getLogger('dataCollector')
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), _CONFIG_FILE_NAME))

warnings.simplefilter("ignore", bs4.XMLParsedAsHTMLWarning, lineno=0)

DOCKERIZED = os.environ.get("DOCKERIZED")
ROUTER_API_ENDPOINT = (f'{config.get("router", "host")}/'
                       f'{config.get("router", "month_statistics_endpoint")}')
FLASK_API_ENDPOINT = (f'{config.get("application", "docker_host" if DOCKERIZED=="true" else "host")}:'
                      f'{config.get("application", "flask_port")}/'
                      f'{config.get("application", "flask_endpoint")}')
JOB_SCHEDULE = int(config.get("application", "data_collector_job_schedule"))


def job():
    """
    A function which is scheduled within specified schedule.
    This function collects usage data from router API and makes
    a proper PUT request to insert it to the database.
    """
    retries = Retry(total=4, status_forcelist=[429, 500, 502, 503, 504],
                    allowed_methods=["GET", "PUT"], backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retries)
    session = Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    logger.info('Collecting usage data')
    try:
        router_api_response = session.get(ROUTER_API_ENDPOINT)
        router_api_response.raise_for_status()
    except (ConnectionError, ConnectionRefusedError, HTTPError, MaxRetryError):
        logger.critical('Unable to collect data, job failed')
        return
    soup = bs4.BeautifulSoup(router_api_response.content, 'lxml')
    current_month_download = convert_b_to_gb(int(soup.find('currentmonthdownload').get_text()))
    current_month_upload = convert_b_to_gb(int(soup.find('currentmonthupload').get_text()))
    time_stamp = datetime.datetime.now(datetime.timezone.utc)
    usage_stamp_data = {'current_month_download': current_month_download,
                        'current_month_upload': current_month_upload,
                        'time_stamp': time_stamp}
    try:
        flask_api_response = session.put(FLASK_API_ENDPOINT, params=usage_stamp_data)
        flask_api_response.raise_for_status()
    except (ConnectionError, ConnectionRefusedError, HTTPError, MaxRetryError):
        logger.critical('Unable to insert data, job failed')
        return
    logger.info('Inserted data: %s', flask_api_response.json())


def convert_b_to_gb(number):
    """
    This function converts (large) number from bytes unit to GB and returns as Decimal type.
    """
    return Decimal(number / 2 ** 30).quantize(Decimal('1.000'))


schedule.every(JOB_SCHEDULE).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
