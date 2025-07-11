from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select(selector="span.titleline > a")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

most_upvotes = max(article_upvotes)
largest_index = article_upvotes.index(most_upvotes)
print("Most popular article:")
print(article_texts[largest_index])
print(article_links[largest_index])
