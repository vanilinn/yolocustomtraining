import json

# Путь к большому JSON файлу
file_path = r'C:\Users\user\PycharmProjects\yolocustomtraining\coco\annotations\instances_val2017.json'


# Функция для извлечения всех ключей из JSON объекта
def extract_keys(data, keys_set):
    if isinstance(data, dict):
        for key, value in data.items():
            keys_set.add(key)
            extract_keys(value, keys_set)
    elif isinstance(data, list):
        for item in data:
            extract_keys(item, keys_set)


# Чтение JSON файла
with open(file_path, 'r') as f:
    data = json.load(f)

# Набор для хранения уникальных ключей
unique_keys = set()
extract_keys(data, unique_keys)

# Вывод всех уникальных ключей
print("Уникальные ключи в JSON файле:")
for key in unique_keys:
    print(key)
