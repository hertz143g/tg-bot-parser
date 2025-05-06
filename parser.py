import requests
from bs4 import BeautifulSoup

def get_news(limit=5):
    url = "https://habr.com/ru/all/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")  # вот эта строка и есть articles!

    news_list = []

    for article in articles[:limit]:
        title_tag = article.find("h2")
        if title_tag:
            title = title_tag.text.strip()
            link = title_tag.find("a")["href"]
            if not link.startswith("http"):
                link = "https://habr.com" + link
            news_list.append((title, link))  # теперь возвращаем кортежи

    return news_list
