from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import AvailableDrivers
PROXY = ''

def start_firefox(url: str) -> webdriver:
    driver = webdriver.Firefox(executable_path=AvailableDrivers.FIREFOX_PATH.value)
    driver.get(url)
    return driver


def start_chrome(url: str) -> webdriver:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-software-rasterizer")
    driver = webdriver.Chrome(executable_path=AvailableDrivers.CHROME_PATH.value, options=chrome_options)
    driver.get(url)
    return driver