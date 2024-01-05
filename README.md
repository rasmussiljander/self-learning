# Self-learning Projects

This repository serves as a hub for miscellaneous self-learning projects related to data and machine learning. Each project is partitioned into its own directory in the repository root. With this, it is easier for me to see the topics that I have already explored and helps me understand what possible gaps I might still have in my understanding. 
This repository is not designed to contain production-grade code or even be structured in a way that is conducive for easy clone-and-run code, but as mentioned, is meant for collecting all different projects and learning opportunities into one :)

Below are short explanations of each project.

### 2D Shape Recognition

`2D_shape_recognition/`

A simple deep learning project, training a convolutional neural network from scratch to classify images into circles, squares, or triangles. The project serves as a quick review of CNNs and helps me refresh what I already learned in school and have something similar that I have implemented in my own.

### Food Orders Forecasting

A very simple SARIMA project that was completed as a task part of a summer internship application in 2021. The project was completed locally but migrated to this repo in 2024. 

### Student Register

`student_register/`

An old (2018) project work for a C programming basics course. 
The project is a simple CLI student register that allows you to add students to a register and dynamically control their information.

### Other projects

**cGANs for MRI modality conversion**

A university group project where we designed a Conditional Generative Adversarial Neural Net (cGAN) for converting the modality (weighting) of MRI brain images. The project was written using `TensorFlow`.
   - Link to private repo : [link](git@github.com:tonipel/mri-modality-conversion.git)
   - TensorFlow description of `pix2pix` algorithm that the model is based on: [pix2pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
   - Conditional Adversarial Nets: [research paper](https://arxiv.org/abs/1611.07004)


### Github Actions

The Github Actions in this repo are mainly used to practice the use of GH Actions. As there is no production code or model maintenance, there will be no model update, automatization, data loading, or other scheduling. 
There are however, some simple checks that are run that help learn Actions. 
There will be more workflows added as needed, but below is the list of current workflows:
- **Jupyter Notebook linting**: The Python code snippets in all repo notebooks are `flake8`, `black` linted using the package `nbqa`. The workflows are supposed to fail if poorly formatted code is detected. The workflows are triggered on all branches for all commmits and pull request activities. There is no separate scheduling for these workflows.
