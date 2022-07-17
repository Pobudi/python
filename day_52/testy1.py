from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
import math
from pprint import pprint


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/")
        #self.driver.maximize_window()

    def login(self):
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        cookies.click()

        time.sleep(5)
        login = self.driver.find_element(By.NAME, "username")
        login.send_keys("kowaltest@yahoo.com")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("Haslo123.")
        time.sleep(5)

        go = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        go.click()

    def find_followers(self):
        time.sleep(5)
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys("schwarzegenegger")

        time.sleep(5)
        schwarzenegger = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        schwarzenegger.click()

        time.sleep(5)
        following = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div')
        following.click()

        number_of_followers = int(self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span').text)
        time.sleep(5)
        frame = self.driver.find_element(By.CLASS_NAME, 'isgrP')

        for _ in range(math.floor(number_of_followers / 6)):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", frame)
            time.sleep(3)

    def follow(self):

        time.sleep(5)
        to_follow = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for follow in to_follow:
            try:
                follow.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                time.sleep(3)
                anuluj = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                anuluj.click()
                time.sleep(2)
                follow.click()


bot = InstagramBot()
bot.login()
bot.find_followers()
bot.follow()
