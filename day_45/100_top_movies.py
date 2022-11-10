from bs4 import BeautifulSoup
import requests

request = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(request.text, "html.parser")

with open("list.txt", "w") as file:
    for title in soup.find_all(name="h3", class_="title")[::-1]:
        file.write(f"{title.string}\n")
