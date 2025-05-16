import logging

logging.basicConfig(
    level=logging.DEBUG,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",   # Log file name
    filemode="a"          # "w" untuk menimpa file, "a" untuk append
)


def divide_numbers(a, b):
    logging.info(f"Memulai pembagian: {a} / {b}")

    try:
        result = a / b
        logging.info(f"Hasil pembagian: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Terjadi error: Pembagian dengan nol")
        return None


# Contoh penggunaan fungsi
divide_numbers(10, 2)
divide_numbers(10, 0)