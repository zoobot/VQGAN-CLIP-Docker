from torch import optim
from core.optimizer import DiffGrad, AdamP, RAdam

from PIL import Image


def resize_image(image, out_size):
    ratio = image.size[0] / image.size[1]
    area = min(image.size[0] * image.size[1], out_size[0] * out_size[1])
    size = round((area * ratio)**0.5), round((area / ratio)**0.5)
    return image.resize(size, Image.LANCZOS)


def get_optimizer(z, optimizer="Adam", step_size=0.1):
    if optimizer == "Adam":
        opt = optim.Adam([z], lr=step_size)     # LR=0.1 (Default)
    elif optimizer == "AdamW":
        opt = optim.AdamW([z], lr=step_size)    # LR=0.2
    elif optimizer == "Adagrad":
        opt = optim.Adagrad([z], lr=step_size)  # LR=0.5+
    elif optimizer == "Adamax":
        opt = optim.Adamax([z], lr=step_size)   # LR=0.5+?
    elif optimizer == "DiffGrad":
        opt = DiffGrad([z], lr=step_size)       # LR=2+?
    elif optimizer == "AdamP":
        opt = AdamP([z], lr=step_size)          # LR=2+?
    elif optimizer == "RAdam":
        opt = RAdam([z], lr=step_size)          # LR=2+?
    return opt
