from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

PROMISED_UP = 100
PROMISED_DOWN = 10
NUMBER = 692530966
PASSWORD = ""

service = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=service)


class Bot:

    def __init__(self):
        self.service = Service("D:\\chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        i_consent = self.driver.find_element(By.ID, '_evidon-banner-acceptbutton')
        i_consent.click()

        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()

        # time.sleep(120)
        # self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.up = 19
        self.down = 18

    def tweet(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        login = self.driver.find_element(By.NAME, 'text')
        login.click()
        login.send_keys("103bartek@gmail.com\t\n")
        time.sleep(5)
        password = driver.find_element(By.NAME, "password")
        password.send_keys("2002warszawka2002")


        # phone_number.send_keys("+48692530966")

twitter_bot = Bot()
twitter_bot.internet_speed()
twitter_bot.tweet()
