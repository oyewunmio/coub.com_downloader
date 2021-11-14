#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

#web driver configuration
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.headless = False
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
ua = UserAgent(use_cache_server=False)
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

        

    except TimeoutException:
        print("Timed out waiting for page to load")

    # driver.close()

send_to_3rd_party('https://coub.com/view/2cg8g7')