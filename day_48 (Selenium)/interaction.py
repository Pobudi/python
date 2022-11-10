from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# number.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.XPATH, "/html/body/form/input[1]")
first_name.send_keys("Bartosz\tPobudejski\t103bartek@gmail.com\t\n")
