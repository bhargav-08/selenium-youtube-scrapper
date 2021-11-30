from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


if __name__=="__main__":

    YOUTUBE_TRENDING = "https://www.youtube.com/feed/trending"

    driver = get_driver()
    driver.get(YOUTUBE_TRENDING)

    print(driver.title)


