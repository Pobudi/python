from bs4 import BeautifulSoup
from pprint import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

service = Service("D:\\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D"
                        "%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C"
                        "%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37"
                        ".857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B"
                        "%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf"
                        "%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B"
                        "%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1"
                        "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")
driver.maximize_window()
time.sleep(5)
for _ in range(20):
    webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
for _ in range(120):
    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

list_of_links = list(set([i.get("href") if i.get("href").startswith("https") else f"https://www.zillow.com{i.get('href')}" for i in soup.findAll(name="a", class_="list-card-link")]))
pprint(list_of_links)
print(f"ilosc znalezionych linkow: {len(list_of_links)}")

list_of_prices = [price.text.split("/")[0] if "/" in price.text else price.text.split("+")[0] for price in soup.findAll(name="div", class_="list-card-price")]
print(list_of_prices)
print(f"ilosc znalezionych cen: {len(list_of_prices)}")

list_of_addresses = [adress.text for adress in soup.findAll(name="address", class_="list-card-addr")]
print(list_of_addresses)
print(f"ilosc znalezionych cen: {len(list_of_addresses)}")

for j in range(40):
    docs_params = {
        "arkusz1": {
            "address": list_of_addresses[j],
            "price": list_of_prices[j],
            "link": list_of_links[j]
        }
    }
    docs_response = requests.post(url="https://api.sheety.co/f3332c757983ae0e3b387fede7579f95/housing/arkusz1", json=docs_params)
    docs_response.raise_for_status()
    print(docs_response.text)

