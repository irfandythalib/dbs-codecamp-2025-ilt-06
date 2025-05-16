import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql


urls = {
    "Quotes": "http://quotes.toscrape.com/",
    "Books": "http://books.toscrape.com/"
}


data = []

# ========== SCRAPING QUOTES TO SCRAPE ==========
response_quotes = requests.get(urls["Quotes"])
if response_quotes.status_code == 200:
    soup_quotes = BeautifulSoup(response_quotes.content, "html.parser")
    quotes_elements = soup_quotes.find_all("div", class_="quote")

    for quote in quotes_elements:
        title = quote.find("span", class_="text").get_text()
        content = quote.find("small", class_="author").get_text()

        data.append({
            "Source": "Quotes",
            "Title": title,
            "Content": content
        })

# ========== SCRAPING BOOKS TO SCRAPE ==========
response_books = requests.get(urls["Books"])
if response_books.status_code == 200:
    soup_books = BeautifulSoup(response_books.content, "html.parser")
    book_elements = soup_books.find_all("article", class_="product_pod")

    for book in book_elements:
        title = book.h3.a["title"]
        content = book.find("p", class_="price_color").get_text()

        data.append({
            "Source": "Books",
            "Title": title,
            "Content": content
        })

# ========== DATABASE MYSQL ==========
try:
    # Koneksi
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="media-online"
    )

    query = "SELECT judul, isi FROM berita"
    df_db = pd.read_sql(query, connection)

    df_db["Source"] = "Database"

    for index, row in df_db.iterrows():
        data.append({
            "Source": "Database",
            "Title": row["judul"],
            "Content": row["isi"]
        })

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals():
        connection.close()

# ========== MENYIMPAN DATA KE CSV ==========

df = pd.DataFrame(data)
output_file = "combined_data.csv"
df.to_csv(output_file, index=False)
print(f"Data berhasil disimpan ke {output_file}")