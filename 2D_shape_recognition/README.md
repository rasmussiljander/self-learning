# 2D shape recognition with basic convolutional neural nets

This projects desings a CNN for basic 2D shape classification from color images.
It takes a dataset of 2D shapes as input and trains a model to classify them into different shape categories,
circles, triangles, or squares. 

## Contents
- [Data](#data)
- [File contents](#file-contents)
- [Architecture](#architecture)
- [Installation](#installation)

## Data

The data was loaded directly from a paper by Korchi and Ganou (2020) linked [here](https://www.sciencedirect.com/science/article/pii/S2352340920309847) 
(they actually also used a CNN to test out the dataset).
The dataset contained 90000 color images of size (200, 200, 3). 
The data contained 9 different shapes equally distributed, meaning that each shape had 10000 examples.

For my use case, I chose to simply choose three shapes, as this was enough for a simple POC of CNNs for basic image classification. 
The shapes I chose were circle, triangle, and square. This left me with a dataset of 30000 that were eventually partitioned into training and test sets using a 80-20% split. 
No separate validation set was annointed.

Note that since the dataset was came from a publication revolving around the definition of this dataset itself, the data was already very curated and it ensured that there was wide range of different examples to train on.
Therefore, no further processing (such as augmentation, rescaling, etc.) was necessary.

## Project contents

The project structure is a bare-bones exploration-type of directory, with two notebooks, a `README.md` file, and a `.yml` for creating a virtual environment where to run the project in.

- `shape_recognition.yml`: File containing the packages for creating the project virtual environment.
- `data_preprocessing.ipynb`: Notebook for data exploration and processing.
   - Visualizing shapes, inspecting lables, distributions of shape categories.
   - Preprocessing for training: loading the images, dropping unwanted data, normalizing pixel values, splitting them into training and test sets
- `cnn.ipynb`: Notebook for building, training, and evaluating the classification model.
   - Builds and trains a basic CNN
   - Evaluates error curves and adds regularization
   - Evaluation of final model trained with full data
- `models/cnn.keras`: Saved trained CNN model. Can be used for testing the final model.




## Architecture

The architecture of the model is a very basic CNN with a couple of convolutional layers, max pooling, and final fully connected layers. 
I have also added a some 20% dropouts to help with overfitting. 
The optizer is Adam with a 0.001 learning rate, and I use categorical cross-entropy as a typical objective function for classification tasks.
The model is trained using `keras`.
For more details, see the `CNN` classes in `cnn.ipynb`.


## Usage 

To ensure stable development, you should run this project inside a model-dedicated Python environment. 
You can use any environment you wish, for example a conda or virtual environment, but I chose to run the notebooks inside a conda environment.
The used packages are found in `shape_recognition.yml`, and you can create the conda environment with the following CLI command:

```
$ conda env create -f shape_recognition.yml
```

To train the model from scratch and run all processes, you should download the data from the link supplied in the [Data](#data) section to the directory `2D_shape_recognition/data/shapes`. Then you can run the cells in the two notebooks in the following order:

1. `data_processing.ipynb`
    - This will download the data, process it, and save it to `processed/` for the model to use.
2. `cnn.ipynb`
    - If you want to save time, you can skip the training the first model, and instead, train the final model labeled `model1`. Training should take about 1h with no acceleration.

If you simply want to prototype the model, you can just download the `keras` model from `models/cnn.keras`.

When inputting and image (remember to make sure its 200x200x3!) to `model.model.predict()`, the output should be approximately something like this:

> [0.42294613 0.57189    0.00516394]

Here each element in the array represents the activation of each shape. 
The prediction itself will be chosen as the element in the array with the highest output value. 
In this case it would be the second element, which represents a `square`. 
The shapes are represented in the array in the following order: `["circle", "square", "triangle"]`.