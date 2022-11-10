from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_links = []

for article in articles:
    article_text.append(article.get_text())
    article_links.append(article.get("href"))

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_text)
print(article_links)
print(article_upvotes)

winning_index = article_upvotes.index(max(article_upvotes))
print(article_text[winning_index])
print(article_links[winning_index])
print(article_upvotes[winning_index])

