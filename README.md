# Скрипт для Обучения YOLOv8 на Датасете COCO

Этот проект включает скрипты для обучения модели YOLOv8 на урезанной версии датасета COCO. Он включает в себя инструменты для преобразования аннотаций в нужный формат и запуск самого процесса обучения.

## Описание

### 1. `filtering1.py`
Скрипт для преобразования аннотаций из формата JSON (COCO) в текстовый формат, используемый для обучения YOLO. 

### 2. `train.py`
Скрипт для запуска процесса обучения модели YOLOv8. Он ожидает наличие аннотаций и изображений в соответствующих папках, указаных ниже.

## Структура Папок

- **`annotations`**: Должны содержать аннотации в формате COCO.
- **`coco/images`**: Содержит изображения, разделенные на папки `train`, `test` и `val`.
- **`coco/labels`**: Должны содержать `.txt` файлы с аннотациями для каждого изображения.

## Стек Технологий

- **Python 3.x**
- **YOLOv8** (Ultralytics)
- **PyTorch** (>=2.3.1+cu121)
- **OpenCV** (>=4.10.0.84)
- **NumPy** (>=1.26.4)
- **Matplotlib** (>=3.9.1)
- **Pandas** (>=2.2.2)
- **SciPy** (>=1.14.0)
- **Seaborn** (>=0.13.2)
- **PyYAML** (>=6.0.1)
- **Ultralytics** (>=8.2.49)

## Установка и Запуск

### 1. Клонирование Репозитория

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
