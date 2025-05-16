import pymysql
import pandas as pd

# Koneksi ke database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="a-media-online-2025"
)

try:
    # Query SQL
    query = "SELECT judul_berita, konten_berita FROM berita"

    # Eksekusi query dan masukkan ke DataFrame
    df = pd.read_sql(query, connection)

    # Ekspor ke CSV
    output_file = "sql-data.csv"
    df.to_csv(output_file, index=False)
    print(f"Data berhasil disimpan ke {output_file}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Tutup koneksi
    connection.close()