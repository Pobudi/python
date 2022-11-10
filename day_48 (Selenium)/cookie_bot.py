from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sevice = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=sevice)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

product0_count = True
product1_count = True
product2_count = True

product0_price = int(driver.find_element(By.XPATH, '//*[@id="productPrice0"]').text)
product0_button = driver.find_element(By.ID, "product0")

product1_price = int(driver.find_element(By.XPATH, '//*[@id="productPrice1"]').text)
product1_button = driver.find_element(By.ID, "product1")

#product2_price = int(driver.find_element(By.ID, '//*[@id="productPrice2"]').text)
#product2_button = driver.find_element(By.ID, "product2")

#product3_price = int(driver.find_element(By.ID, '//*[@id="productPrice3"]').text)
#product3_button = driver.find_element(By.ID, "product3")

while True:
    number_cookies = int(driver.find_element(By.ID, "cookies").text.split("\n")[0].split(" ")[0])
    cookie.click()
    if number_cookies > product0_price and product0_count:
        product0_button.click()
        product0_count = False
    elif number_cookies > product1_price and product1_count:
        product1_button.click()
        product1_count = False
        '''
    elif number_cookies > product2_price and product2_count:
        product2_button.click()
        product2_count = False
    elif number_cookies > product3_price:
        product3_button.click()
        product0_count = True
        product1_count = True
        product2_count = True
        '''