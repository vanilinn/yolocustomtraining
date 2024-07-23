import json
import os

# Загрузка COCO аннотаций из файла
with open(r'C:\Users\user\PycharmProjects\yolocustomtraining\coco\annotations\instances_val2017.json', 'r') as f:
    coco_data = json.load(f)

# Путь к папке, куда будут сохраняться файлы с аннотациями YOLO
output_dir = 'val_labels'
os.makedirs(output_dir, exist_ok=True)

# Стандартные категории COCO
coco_categories = [
    {"id": 1, "name": "person"}, {"id": 2, "name": "bicycle"}, {"id": 3, "name": "car"},
    {"id": 4, "name": "motorcycle"}, {"id": 5, "name": "airplane"}, {"id": 6, "name": "bus"},
    {"id": 7, "name": "train"}, {"id": 8, "name": "truck"}, {"id": 9, "name": "boat"},
    {"id": 10, "name": "traffic light"}, {"id": 11, "name": "fire hydrant"}, {"id": 12, "name": "stop sign"},
    {"id": 13, "name": "parking meter"}, {"id": 14, "name": "bench"}, {"id": 15, "name": "bird"},
    {"id": 16, "name": "cat"}, {"id": 17, "name": "dog"}, {"id": 18, "name": "horse"},
    {"id": 19, "name": "sheep"}, {"id": 20, "name": "cow"}, {"id": 21, "name": "elephant"},
    {"id": 22, "name": "bear"}, {"id": 23, "name": "zebra"}, {"id": 24, "name": "giraffe"},
    {"id": 25, "name": "backpack"}, {"id": 26, "name": "umbrella"}, {"id": 27, "name": "handbag"},
    {"id": 28, "name": "tie"}, {"id": 29, "name": "suitcase"}, {"id": 30, "name": "frisbee"},
    {"id": 31, "name": "skis"}, {"id": 32, "name": "snowboard"}, {"id": 33, "name": "sports ball"},
    {"id": 34, "name": "kite"}, {"id": 35, "name": "baseball bat"}, {"id": 36, "name": "baseball glove"},
    {"id": 37, "name": "skateboard"}, {"id": 38, "name": "surfboard"}, {"id": 39, "name": "tennis racket"},
    {"id": 40, "name": "bottle"}, {"id": 41, "name": "wine glass"}, {"id": 42, "name": "cup"},
    {"id": 43, "name": "fork"}, {"id": 44, "name": "knife"}, {"id": 45, "name": "spoon"},
    {"id": 46, "name": "bowl"}, {"id": 47, "name": "banana"}, {"id": 48, "name": "apple"},
    {"id": 49, "name": "sandwich"}, {"id": 50, "name": "orange"}, {"id": 51, "name": "broccoli"},
    {"id": 52, "name": "carrot"}, {"id": 53, "name": "hot dog"}, {"id": 54, "name": "pizza"},
    {"id": 55, "name": "donut"}, {"id": 56, "name": "cake"}, {"id": 57, "name": "chair"},
    {"id": 58, "name": "couch"}, {"id": 59, "name": "potted plant"}, {"id": 60, "name": "bed"},
    {"id": 61, "name": "dining table"}, {"id": 62, "name": "toilet"}, {"id": 63, "name": "tv"},
    {"id": 64, "name": "laptop"}, {"id": 65, "name": "mouse"}, {"id": 66, "name": "remote"},
    {"id": 67, "name": "keyboard"}, {"id": 68, "name": "cell phone"}, {"id": 69, "name": "microwave"},
    {"id": 70, "name": "oven"}, {"id": 71, "name": "toaster"}, {"id": 72, "name": "sink"},
    {"id": 73, "name": "refrigerator"}, {"id": 74, "name": "book"}, {"id": 75, "name": "clock"},
    {"id": 76, "name": "vase"}, {"id": 77, "name": "scissors"}, {"id": 78, "name": "teddy bear"},
    {"id": 79, "name": "hair drier"}, {"id": 80, "name": "toothbrush"}
]

# Фильтруем только первые 70 категорий
valid_category_ids = set(cat['id'] for cat in coco_categories[:70])

# Создаем словарь для быстрого доступа к данным изображения по id
images = {image['id']: image for image in coco_data['images']}

# Обрабатываем аннотации
for annotation in coco_data['annotations']:
    image_id = annotation['image_id']
    coco_category_id = annotation['category_id']

    # Фильтруем только категории, идентификаторы которых в пределах 1-70
    if coco_category_id not in valid_category_ids:
        continue  # Пропускаем аннотацию, если категория не соответствует условию

    # Переопределяем идентификатор категории для YOLO (0-69 вместо 1-70)
    yolo_category_id = coco_category_id - 1

    # Получаем размеры изображения
    image = images[image_id]
    image_width = image['width']
    image_height = image['height']

    # Получаем координаты и размеры объекта
    bbox = annotation['bbox']
    x, y, width, height = bbox

    # Рассчитываем центр и нормализуем координаты
    center_x = (x + width / 2) / image_width
    center_y = (y + height / 2) / image_height
    norm_width = width / image_width
    norm_height = height / image_height

    # Формируем строку для записи в файл
    yolo_annotation = f"{yolo_category_id} {center_x} {center_y} {norm_width} {norm_height}\n"

    # Имя файла для аннотаций текущего изображения
    annotation_filename = os.path.join(output_dir, f"{os.path.splitext(image['file_name'])[0]}.txt")

    # Записываем аннотацию в файл
    with open(annotation_filename, 'a') as f:
        f.write(yolo_annotation)
