from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

events = {}
wiadomosc = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
lista = wiadomosc.text.split("\n")
print(lista)
for count, element in enumerate(lista[::2]):
    events[count] = dict({"time": element, "name": lista[lista.index(element)+1]})

print(events)
driver.close()