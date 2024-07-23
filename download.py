import requests
from pathlib import Path
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Функция для скачивания файла
def download_file(url, dest_folder):
    local_filename = url.split('/')[-1]
    local_path = Path(dest_folder) / local_filename

    # # Настройки прокси
    # proxies = {
    #     'http': 'socks5://72.217.211.3:4145',
    #     'https': 'socks5://72.217.211.3:4145'
    # }

    try:
        logging.info(f"Начинаем скачивание файла {local_filename} из {url}")

        # Скачивание файла с использованием прокси
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_length = r.headers.get('content-length')
            if total_length is None:  # нет заголовка content-length
                total_length = 0
            else:
                total_length = int(total_length)

            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded = f.tell()
                    progress = downloaded / total_length * 100 if total_length else 0
                    logging.info(f"Скачивание {local_filename}: {downloaded} из {total_length} байт ({progress:.2f}%)")

        logging.info(f"Файл {local_filename} загружен в {local_path}")
        return local_path
    except Exception as e:
        logging.error(f"Ошибка при скачивании {url}: {e}")
        raise


# URLs для скачивания
urls = [
    'http://images.cocodataset.org/zips/train2017.zip',
    'http://images.cocodataset.org/zips/val2017.zip',
    'http://images.cocodataset.org/zips/test2017.zip',
    'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
]

# Папка для сохранения файлов
destination_folder = r'C:\Users\user\PycharmProjects\yolocustomtraining\coco'

# Создание папки, если не существует
Path(destination_folder).mkdir(parents=True, exist_ok=True)

# Скачивание файлов
for url in urls:
    try:
        download_file(url, destination_folder)
    except Exception as e:
        logging.error(f"Ошибка при скачивании {url}: {e}")
