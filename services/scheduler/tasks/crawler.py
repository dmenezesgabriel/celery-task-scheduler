from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.extensions import celery


def set_chrome_options() -> None:
    """
    Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls print_arg('hello') every 2 seconds.
    sender.add_periodic_task(
        120.0, crawler.s("http://www.python.org"), name="Crawler"
    )


@celery.task()
def crawler(arg):
    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(arg)
    title = driver.title
    driver.close()
    print(title)
    return title
