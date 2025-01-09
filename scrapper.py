# python -m pip install requests
# => get data drom web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

# install git
# create repository

# go to git hub 
# git config --global user.name"manishchy53"
# git config --global user.name"manishchaudhary206153@gmail.com"

# git init
# git status => if you want to check what are the status of file
# git diff => if you want to check what are the changes
# git add .
# git commit -m "your message"
# git push origin => update the code 
# copy paste git from code

##################################
# 1. change the code
# 2. git add .
# 3. git commit -m "your message"
# 4. git push origin 
##################################


# This is the git codes branch

import json 
import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error")
        return

    # set encoding explicity to handle special character
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    all_books = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1: ]
        formatted_book = {
            "title": title,
            "currency": currency,
            "price": price,
        }
        all_books.append(formatted_book)

    return all_books

scrape_books(URL) 

books = scrape_books(URL)
with open("books.json", "w") as f:
    json.dump(books, f,indent=4)