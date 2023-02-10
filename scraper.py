from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import bs4


driver = uc.Chrome(use_subprocess=True)
for x in range(1,650):
    driver.get("https://www.futbin.com/players?page="+str(x))
    # Waiting for class element to load to stop loading the whole page
    w = WebDriverWait(driver, 15)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, "player_tr_1")))
    # Parsing page HTML to BeautifulSoup
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    numbers = [1,2]
    players = []
    # Extracting all player links from html using BeautifulSoup
    for number in numbers:
        players.extend(soup.findAll('tr', 'player_tr_'+str(number)))
    print('Found {} players in page {}'.format(len(players), x))
    # Writing player links to file
    for player in players:
        with open("playerLinks.txt", 'a') as file:
            file.write("https://www.futbin.com"+player['data-url']+"\n")