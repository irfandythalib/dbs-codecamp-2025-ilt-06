import requests
from bs4 import BeautifulSoup

# URL target
# url = "https://medium.com"
url = "https://kalla.co.id"


# Mengirim request ke URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
# # Cek status kode
# if response.status_code == 200:
#     # Parsing HTML
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Mencari semua elemen <h2> yang biasanya berisi judul artikel
#     titles = soup.find_all("h2")
#
#     # Menampilkan judul artikel
#     print("Judul Artikel di Medium:")
#     for idx, title in enumerate(titles, start=1):
#         print(f"{idx}. {title.get_text()}")
# else:
#     print(f"Gagal mengakses halaman. Status code: {response.status_code}")