from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class InstagramBot:
    def __init__(self):
        service = Service("D:\\chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        time.sleep(0)

    def login(self):
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        cookies.click()

        login = self.driver.find_element(By.NAME, "username")
        login.send_keys("makowal3024@gmail.com\tHaslo123.\t\n")
    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstagramBot()
bot.login()
bot.find_followers()
bot.follow()
