import json

# Путь к исходному файлу аннотаций
input_file_path = r'C:\Users\user\PycharmProjects\yolocustomtraining\coco\annotations\instances_train2017.json'

# Путь для сохранения отфильтрованного файла аннотаций
output_file_path = r'C:\Users\user\PycharmProjects\yolocustomtraining\coco\annotations\instances_train2017_filtered.json'

# Загружаем исходный файл аннотаций
with open(input_file_path, 'r') as f:
    annotations = json.load(f)

# Идентификаторы классов, которые нужно исключить
excluded_categories = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

# Получаем список всех категорий
categories = annotations['categories']

# Определяем категории, которые не нужно исключать
included_categories = [cat for cat in categories if cat['id'] not in excluded_categories]

# Создаем словарь для преобразования category_id
category_mapping = {cat['id']: cat['id'] for cat in included_categories}

# Количество аннотаций до фильтрации
original_annotations_count = len(annotations['annotations'])

# Отфильтровываем аннотации
filtered_annotations = [ann for ann in annotations['annotations'] if ann['category_id'] in category_mapping]

# Количество аннотаций после фильтрации
filtered_annotations_count = len(filtered_annotations)

print(f"Количество аннотаций до фильтрации: {original_annotations_count}")
print(f"Количество аннотаций после фильтрации: {filtered_annotations_count}")

# Создаем новый JSON с отфильтрованными аннотациями
filtered_annotations_json = {
    'info': annotations['info'],
    'licenses': annotations['licenses'],
    'images': annotations['images'],
    'annotations': filtered_annotations,
    'categories': included_categories
}

# Сохраняем отфильтрованный файл
with open(output_file_path, 'w') as f:
    json.dump(filtered_annotations_json, f, indent=2)

print("Фильтрация завершена. Отфильтрованный файл сохранен.")
