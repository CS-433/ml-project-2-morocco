import torch
from src.SPIN.model import SPINRoadMapper, SPINRoadMapperFCN8
import torchvision.models.segmentation as segmentation


DATA_PATH = "dataset/"
TRAIN_IMAGES_PATH = DATA_PATH + "training/images/"
TRAIN_MASKS_PATH = DATA_PATH + "training/groundtruth/"
TEST_IMAGES_PATH = DATA_PATH + "test_set_images/"

# Parameters
MODEL = SPINRoadMapper(model_func=segmentation.DeepLabV3_ResNet101_Weights, weights=segmentation.DeepLabV3_ResNet101_Weights)
BATCH_SIZE = 16
LEARNING_RATE = 1e-4
EPOCHS = 30
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {DEVICE}")