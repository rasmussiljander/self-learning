# 2D shape recognition with basic convolutional neural nets

# To install the required environment, you can use the provided YAML file.
# Follow the steps below to set up the environment:
This projects desings a CNN for basic 2D shape classification from color images.
It takes a dataset of 2D shapes as input and trains a model to classify them into different shape categories,
circles, triangles, or squares. 

# 1. Create a new virtual environment (optional but recommended):
#    $ python -m venv shape_recognition_env
#    $ source shape_recognition_env/bin/activate
## Contents
- [Data](#data)
- [File contents](#file-contents)
- [Architecture](#architecture)
- [Installation](#installation)

## Data

# 2. Install the required packages using the provided YAML file:
#    $ conda env create -f environment.yml
The data was loaded directly from a paper by Korchi and Ganou (2020) linked [here](https://www.sciencedirect.com/science/article/pii/S2352340920309847) 
(they actually also used a CNN to test out the dataset).
The dataset contained 90000 color images of size (200, 200, 3). 
The data contained 9 different shapes equally distributed, meaning that each shape had 10000 examples.

# 3. Activate the environment:
#    $ conda activate shape_recognition_env
For my use case, I chose to simply choose three shapes, as this was enough for a simple POC of CNNs for basic image classification. 
The shapes I chose were circle, triangle, and square. This left me with a dataset of 30000 that were eventually partitioned into training and test sets using a 80-20% split. 
No separate validation set was annointed.

# 4. Run the code:
#    $ python shape_recognition.py
Note that since the dataset was came from a publication revolving around the definition of this dataset itself, the data was already very curated and it ensured that there was wide range of different examples to train on.
Therefore, no further processing (such as augmentation, rescaling, etc.) was necessary.

## Project contents

# Note: Make sure you have the necessary dependencies installed, such as Python, Conda, and the required packages specified in the YAML file.
"""
This function/class/module does XYZ.
The project structure is a bare-bones exploration-type of directory, with two notebooks, a `README.md` file, and a `.yml` for creating a virtual environment where to run the project in.

Parameters:
- param1: Description of param1.
- param2: Description of param2.
- `shape_recognition.yml`: File containing the packages for creating the project virtual environment.
- `data_preprocessing.ipynb`: Notebook for data exploration and processing.
   - Visualizing shapes, inspecting lables, distributions of shape categories.
   - Preprocessing for training: loading the images, dropping unwanted data, normalizing pixel values, splitting them into training and test sets
- `cnn.ipynb`: Notebook for building, training, and evaluating the classification model.
   - Builds and trains a basic CNN
   - Evaluates error curves and adds regularization
   - Evaluation of final model trained with full data
- `models/cnn.keras`: Saved trained CNN model. Can be used for testing the final model.

Returns:
Description of the return value(s).

Raises:
Any exceptions that may be raised.

Examples:
>>> example_function(1, 2)
Output: 3
"""
# 2D Shape Recognition

This project is an implementation of a machine learning model for 2D shape recognition. It aims to classify different shapes, such as circles, squares, triangles, and rectangles, based on their visual features.
## Architecture

## Installation
The architecture of the model is a very basic CNN with a couple of convolutional layers, max pooling, and final fully connected layers. 
I have also added a some 20% dropouts to help with overfitting. 
The optizer is Adam with a 0.001 learning rate, and I use categorical cross-entropy as a typical objective function for classification tasks.
The model is trained using `keras`.
For more details, see the `CNN` classes in `cnn.ipynb`.

To run this project, you need to have the following dependencies installed:

- Python 3.x
- NumPy
- OpenCV
- Scikit-learn

You can install the required packages by running the following command:
