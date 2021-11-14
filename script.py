#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


pathname = input('Enter the name of the folder to store the downloaded images to\t')

#web driver configuration
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.headless = False
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
ua = UserAgent(use_cache_server=False)

#file managing configuration
if not os.path.isdir(pathname):
    os.makedirs(pathname)
    prefs = {"profile.managed_default_content_settings.images": 2, 'download.default_directory' : os.path.join(os.getcwd(), pathname)}
    chrome_options.add_experimental_option("prefs", prefs)
else:
    prefs = {"profile.managed_default_content_settings.images": 2, 'download.default_directory' : os.path.join(os.getcwd(), pathname)}

userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def send_to_3rd_party(coub_url):

    #third party application
    url = 'https://savieo.com/sites/coub/'

    driver.get(url)
    timeout = 10

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/main/div/div/div[2]/form/input'))
        WebDriverWait(driver, timeout).until(element_present)
        
        search_bar = driver.find_element(By.XPATH, '//input[@class="w-full text-xl md:text-2xl font-medium dark:text-white placeholder-gray-400 bg-transparent focus:outline-none"]')
        search_bar.send_keys(coub_url)
        search_bar.send_keys(Keys.ENTER)

        
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/main/div[3]/div/div[2]/div/div[2]/div/button[2]'))
        WebDriverWait(driver, timeout).until(element_present)

        download_mp4 = driver.find_element(By.XPATH, '//button[@class="py-3.5 w-full font-bold rounded-md focus:outline-none disabled:cursor-not-allowed mt-4 text-white bg-red-500 dark:bg-red-600 hover:bg-red-600 dark:hover:bg-red-700 disabled:text-white dark:disabled:text-gray-900 disabled:bg-gray-300 dark:disabled:bg-gray-700"]')
        download_mp4.send_keys(Keys.ENTER)

    except TimeoutException:
        print("Timed out waiting for page to load..check your network connectivty")

    # driver.close()

direct_link = input('Enter the link of the coub video to download')


# calling main function
send_to_3rd_party(direct_link)
