from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
c = DesiredCapabilities.CHROME
c["pageLoadStrategy"] = "none"

import bs4

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", desired_capabilities=c)
for x in range(1,10):
    w = WebDriverWait(driver, 15)
    driver.get("https://www.futbin.com/players?page="+str(x))
    w.until(lambda driver: driver.find_elements(By.CLASS_NAME, "player_tr_1") and driver.find_elements(By.CLASS_NAME, "player_tr_2"))
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    numbers = [1,2]
    print("Currently in page {}".format(x))
    for number in numbers:
        players = soup.findAll('tr', 'player_tr_'+str(number))
    print('Found {} players in page {}'.format(len(players), x))
    counter = 0
    for player in players:
        with open("playerLinks.txt", 'a') as file:
            file.write("https://www.futbin.com"+player['data-url']+"\n")
        #print(player['data-url'])