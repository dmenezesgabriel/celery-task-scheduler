import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.extensions import celery

options = Options()
options.headless = True


def set_browser():
    firefox_profile = webdriver.FirefoxProfile()
    return webdriver.Firefox(options=options, firefox_profile=firefox_profile)


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls print_arg('hello') every 2 seconds.
    sender.add_periodic_task(
        120.0, crawler.s("http://www.python.org"), name="Crawler"
    )


@celery.task()
def crawler(arg):
    browser = set_browser()
    browser.get(arg)
    browser.get(arg)
    title = browser.title
    browser.close()
    print(title)
    return title
