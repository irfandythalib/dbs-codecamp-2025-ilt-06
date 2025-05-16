import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# # Cek status kode
if response.status_code == 200:
    # Mencari semua elemen <h3>
    # titles = soup.find_all("h3")
    # for idx, title in enumerate(titles, start=1):
    #     print(f"{idx}. {title.get_text()}")

    # CSS Selecter <p> di dalam .content
    paragraphs = soup.select(".product_pod > h3 > a")
    for p in paragraphs:
        print(p.get_text())
else:
    print(f"Gagal mengakses halaman. Status code: {response.status_code}")