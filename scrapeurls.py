import cloudscraper
from bs4 import BeautifulSoup
import csv
from time import sleep

scraper = cloudscraper.create_scraper()
mealtype = ["breakfast", "desserts", "salads", "soups", "main-course", "bread-recipes"]
for k in range(len(mealtype)):
    site = (
        "https://www.halfbakedharvest.com/category/recipes/type-of-meal/"
        + mealtype[k]
        + "/"
    )
    url = site
    response = scraper.get(url)
    html = response.text
    filename = mealtype[k] + "-links.csv"
    with open(filename, "w") as f:
        soup = BeautifulSoup(html, "lxml")
        writer = csv.writer(f)
        for articles in soup.find_all("article"):
            writer.writerow([articles.a["href"]])

    with open(filename, "a") as f:
        for i in range(2, 30):
            url = site + "page/" + str(i) + "/"
            print(url)
            response = scraper.get(url)
            html = response.text
            soup = BeautifulSoup(html, "lxml")
            writer = csv.writer(f)
            for articles in soup.find_all("article"):
                writer.writerow([articles.a["href"]])
    sleep(5)
