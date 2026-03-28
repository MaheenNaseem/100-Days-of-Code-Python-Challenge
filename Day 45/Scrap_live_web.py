from bs4 import BeautifulSoup
import requests

responses = requests.get("https://news.ycombinator.com/news")
content = responses.text

soup = BeautifulSoup(content, "html.parser")
articles_tag= soup.select(selector= ".titleline > a")
articles_score = [tags.getText() for tags in soup.select(".score")]
article_list= []

for i,tag in enumerate(articles_tag):
    articles_text = tag.getText()
    articles_link = tag.get("href")

    if i < len(articles_score):
        score = articles_score[i]
    else:
        score = "0 points"

    article_list.append({
        "Heading" : articles_text,
        "Score" : score,
        "Link" : articles_link
    })

# for i in article_list:
#     print(article_list)
print(article_list)

