import schedule
import time
import datetime

def job():
    print(f"Script dijalankan pada: {datetime.datetime.now()}")

# Jalankan setiap 5 detik
schedule.every(5).seconds.do(job)

# Jalankan setiap hari pada jam tertentu
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)