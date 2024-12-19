# Project B: Semantic Segmentation for Road Detection

## Project Overview
This project explores semantic segmentation techniques for road detection in aerial imagery. Using various architectures, including U-Net, FPN, and SPINFCN8, the project evaluates their performance on a road segmentation dataset. The results demonstrate the effectiveness of advanced segmentation models in achieving high accuracy and F1 scores.

---

## Table of Contents
1. [Dataset](#dataset)
2. [Implemented Architectures](#implemented-architectures)
3. [How to Run](#how-to-run)
4. [Results](#results)
5. [Ethical Considerations](#ethical-considerations)
6. [Acknowledgments](#acknowledgments)

---

## Dataset
- **Source:** AIcrowd Road Segmentation Challenge.
- **Details:** The dataset consists of:
  - 100 training images with masks.
  - 50 test images without labels.
- **Image Specifications:**
  - Size: 400x400 pixels.
  - Channels: RGB.

### Download Instructions
To download the dataset, follow these steps:
1. Navigate to the [AIcrowd Road Segmentation Challenge](https://www.aicrowd.com/challenges/epfl-ml-road-segmentation).
2. Log in with your credentials. If you do not have an account, create one using your institutional email.
3. Download the dataset files:
   - `train.zip` (contains training images and masks).
   - `test.zip` (contains test images).
4. Extract the downloaded files:
   ```bash
   unzip train.zip -d data/training
   unzip test.zip -d data/test_set_images
### Creating the Validation Set
The dataset does not include a predefined validation set. To create one:

1. Split the `train` directory into:
   - A **training subset** containing 90% of the images and masks.
   - A **validation subset** containing the remaining 10%.

2. Manually move the selected files into the following structure:
````bash
data/
├── training/
│   ├── images/  # Training images
│   └── groundtruth/   # Corresponding segmentation masks
├── validation/
│   ├── images/  # Validation images
│   └── groundtruth/   # Corresponding segmentation masks
└── test/
    └── test_set_images/  # Test images
````

### Preprocessing Steps
- Normalization of pixel values.
- Data augmentation techniques such as flipping and rotation.
- Splitting the training set into 90% training and 10% validation subsets.

---

## Implemented Architectures
### 1. Custom U-Net
- Baseline model implemented from scratch.
- Encoder-decoder structure with skip connections.

### 2. Advanced Architectures (via `smp` Library)
- **FPN:** Multiscale feature aggregation.
- **DeepLabV3+:** Atrous Spatial Pyramid Pooling (ASPP).
- **Encoder**: ResNet50, some with pretrained weights.

### 3. SPINFCN8
- Optimized for efficient and accurate segmentation.
- Combines spatial pyramids with fully convolutional layers.

---

## How to Run

### Prerequisites
- Python 3.8 or later.
- Required libraries: `numpy`, `pytorch`, `torchvision`, `segmentation_models_pytorch`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/CS-433/ml-project-2-morocco
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Create a directory structure for storing the results of the predictions and model checkpoints (model.pth). Run the following commands in your terminal:
   ```bash
   mkdir -p results/current/predictions
   ```



5. For each model, you can adjust the model’s hyperparameters and select the backbone in `config.py`. For optimal performance as demonstrated in our tests, use the configurations specified in `best_config.py` (copy paste in `config.py`) for the SPIN model.

6. In src/SPIN/config.py you can change the variable MODEL which by default is SPINRoadMapperFCN8() but you can also use SPINRoadMapper() with a speicfic backbone and weight (example : MODEL = SPINRoadMapper(model_func=segmentation.deeplabv3_resnet101, weights=segmentation.DeepLabV3_ResNet101_Weights))

6. To test a new model change the model name in the `run.py` file (in the case of SMP change model_name too):
   ```python
   model = 'SPIN' // 'UNET' // 'SMP'
   model_name = 'FPN' // 'UNET' // 'UNET_PRETRAINED'
   ```

7. Run the training script:
   ```bash
   python run.py
   ```


---

## Results

### Quantitative Metrics
| Model        | F1 score (%) | Pixel Accuracy (%) |
|--------------|---------|--------------------|
| Custom U-Net | 74.5    | 81.6               |
| SMP U-Net (pretrained weights)          | 78.3    | 87.8              |
| SPIN + DeepLabV3+     | 87.2   | 93.0               |
| SPIN + FCN8     | 87.9   | 93.3               |
---

## Ethical Considerations

### Potential Risks
- Misuse in surveillance and military applications.

### Mitigation Steps
- Limited the scope to civilian road segmentation applications.
- Ensured the dataset contains no personally identifiable information.

---

## Acknowledgments
- **Course:** Machine Learning (CS-433), EPFL.
- **Libraries:** `segmentation_models_pytorch`, PyTorch.
- **Dataset:** AIcrowd Road Segmentation Challenge.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

