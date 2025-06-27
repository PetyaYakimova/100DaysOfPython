import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = [movie.getText() for movie in soup.select("h2 strong")]
all_movies = all_movies[::-1]

with open("movies.txt", mode="w") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
