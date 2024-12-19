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
3. Run the training script:
   ```bash
   python run.py
   ```

4. To test a new model change the model name in the `run.py` file (in the case of SMP change model_name too):
   ```python
   model = 'SPIN' // 'UNET' // 'SMP'
   model_name = 'FPN' // 'UNET' // 'UNET_PRETRAINED'
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

