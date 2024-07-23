import os

# Добавляем путь к CUDA
os.add_dll_directory(r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\bin')
import torch
from ultralytics import YOLO

# Проверка доступности CUDA
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# Initialize YOLOv8 model
# model = YOLO('yolov8m.pt')
model = torch.load('yolov8m.pt')

# Путь к обновленному конфигурационному файлу
updated_config_file = r'C:\Users\user\PycharmProjects\yolocustomtraining\yolov8.yaml'

# Параметры тренировки
training_params = {
    'data': updated_config_file,  # Путь к обновленному YAML файлу
    'epochs': 10,
    'batch': 16,
    'imgsz': 640,
    'name': 'yolov8m_coco_filtered',
    'device': device,
    'workers': 8,
    'project': None,
    'exist_ok': False,
    'pretrained': True,
    'optimizer': 'auto',
    'verbose': True,
    'seed': 0,
    'deterministic': True,
    'single_cls': False,
    'rect': False,
    'cos_lr': False,
    'close_mosaic': 10,
    'resume': False,
    'amp': True,
    'fraction': 1.0,
    'profile': False,
    'freeze': None,
    'multi_scale': False,
    'overlap_mask': True,
    'mask_ratio': 4,
    'dropout': 0.0,
    'val': True,
    'split': 'val',
    'save_json': False,
    'save_hybrid': False,
    'conf': None,
    'iou': 0.7,
    'max_det': 300,
    'half': False,
    'dnn': False,
    'plots': True,
    'source': None,
    'vid_stride': 1,
    'stream_buffer': False,
    'visualize': False,
    'augment': False,
    'agnostic_nms': False,
    'classes': None,
    'retina_masks': False,
    'embed': None,
    'show': False,
    'save_frames': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'show_labels': True,
    'show_conf': True,
    'show_boxes': True,
    'line_width': None,
    'format': 'torchscript',
    'keras': False,
    'optimize': False,
    'int8': False,
    'dynamic': False,
    'simplify': False,
    'opset': None,
    'workspace': 4,
    'nms': False,
    'lr0': 0.01,
    'lrf': 0.01,
    'momentum': 0.937,
    'weight_decay': 0.0005,
    'warmup_epochs': 3.0,
    'warmup_momentum': 0.8,
    'warmup_bias_lr': 0.1,
    'box': 7.5,
    'cls': 0.5,
    'dfl': 1.5,
    'pose': 12.0,
    'kobj': 1.0,
    'label_smoothing': 0.0,
    'nbs': 64,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'degrees': 0.0,
    'translate': 0.1,
    'scale': 0.5,
    'shear': 0.0,
    'perspective': 0.0,
    'flipud': 0.0,
    'fliplr': 0.5,
    'bgr': 0.0,
    'mosaic': 1.0,
    'mixup': 0.0,
    'copy_paste': 0.0,
    'auto_augment': 'randaugment',
    'erasing': 0.4,
    'crop_fraction': 1.0,
    'cfg': None,
    'tracker': 'botsort.yaml',
    'save_dir': 'runs\\detect\\yolov8m_coco_filtered',
}

if __name__ == '__main__':
    # Start training
    model.train(**training_params)
