import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL target
url = "https://books.toscrape.com/"

# Mengirim request ke URL
response = requests.get(url)

# Cek status kode
if response.status_code == 200:
    # Parsing HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Mencari semua elemen yang mengandung judul buku
    book_elements = soup.find_all("article", class_="product_pod")

    # List untuk menyimpan data
    book_titles = []
    book_links = []

    # Loop melalui setiap elemen buku
    for book in book_elements:
        # Mengambil judul buku
        title = book.h3.a["title"]
        book_titles.append(title)

        # Mengambil link buku
        link = book.h3.a["href"]
        # Membuat link lengkap
        full_link = url + link
        book_links.append(full_link)

    # Membuat DataFrame
    data = {
        "Title": book_titles,
        "Link": book_links
    }
    df = pd.DataFrame(data)

    # Menyimpan ke CSV
    output_file = "books.csv"
    df.to_csv(output_file, index=False)
    print(f"Data berhasil disimpan ke {output_file}")

else:
    print(f"Gagal mengakses halaman. Status code: {response.status_code}")