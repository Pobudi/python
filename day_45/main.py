from bs4 import BeautifulSoup

with open("./website.html") as website:
    text = website.read()

soup = BeautifulSoup(text, "html.parser")
print(soup.title)           # <title>Angela's Personal Site</title>
print(soup.title.string)    # Angela's Personal Site
print(soup.title.name)      # title
print(soup.prettify())
print(soup.a)               # pierwszy anchor

all_anchors = soup.find_all(name="a")

for tag in all_anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")   # szukam anchor ktory siedzi w paragrafie

headings = soup.select(selector=".heading")     # szuakam wszystkiego co ma klase "heading"
