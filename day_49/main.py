from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2912405873&f_AL=true&keywords=korepetytor")
driver.maximize_window()

log_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
log_in.click()

mail = driver.find_element(By. XPATH, '//*[@id="username"]')
mail.send_keys("testkowal123@gmail.com\thaslomaslo\t\t\t\n")

offers = driver.find_elements(By.CLASS_NAME, 'job-card-container')
offers_num = len(offers)

time.sleep(2)
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(2)
for offer in range(offers_num):
    offers[offer].click()
    save = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    time.sleep(2)
    save.click()

