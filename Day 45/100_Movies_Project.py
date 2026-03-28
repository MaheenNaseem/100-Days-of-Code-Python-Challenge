from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text
soup = BeautifulSoup(content,"html.parser")

movie_name = soup.find_all(name="h3", class_="title")

movie_list = [tag.getText() for tag in movie_name]
movie_list = movie_list[::-1]

with open("Top 10 Movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
