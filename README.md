
# Road Segmentation Project README

This README provides instructions on how to set up and run the SPIN road segmentation model for generating predicted segmentation masks of road images.

## Prerequisites

Before running the model, ensure that you have Python installed on your system. This project was developed using Python 3.8, but it should be compatible with other Python 3 versions.

## Setup Instructions

### Step 1: Install Required Libraries

Install all required Python libraries listed in `requirements.txt`. You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 2: Prepare Directory Structure

Create a directory structure for storing the results of the predictions and model checkpoints. Run the following commands in your terminal:

```bash
mkdir -p results/predictions
mkdir -p results/checkpoints
```

### Step 3: Configure the Model

You can adjust the model’s hyperparameters and select the backbone in `config.py`. For optimal performance as demonstrated in our tests, use the configurations specified in `best_config.py`.

### Step 4: Select the Model in `run.py`

In `run.py`, ensure that the SPIN model is selected. This model has shown to provide the best results during our experiments:

```python
model = SPINRoadMapper(model_func, weights, num_classes=1)
```

### Step 5: Run the Model

Execute the script from your terminal to start the training and prediction process:

```bash
python run.py
```

This command will generate predicted images in the `results/predictions` directory and save model checkpoints in `results/checkpoints`.

### Step 6: Generate Submission File

After generating the predicted masks, run the following script to convert these masks into a submission format:

```bash
python submission/mask_to_submission.py
```

This script will produce a `submission.csv` file in the `submission` directory, which you can submit to the competition or use for evaluation purposes.

## Additional Information

- Ensure all scripts are executable and paths in the scripts are correctly set relative to the project directory.
- If you encounter any issues with model training or predictions, check the Python and library versions against the versions listed in `requirements.txt`.

For any further assistance or inquiries, please contact the project maintainer or refer to the documentation provided in the source files.
