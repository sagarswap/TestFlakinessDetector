# Flaky vs Nonflaky Classifier

## Overview
This project contains a Python script for training a neural network to classify data into two categories: Nonflaky (0) and Flaky (1). The model is built using TensorFlow and Keras and is trained on a dataset that is assumed to be preprocessed and saved as `processed_data.csv`.

## Requirements
- Python 3.x
- Pandas
- NumPy
- TensorFlow
- Scikit-Learn
- Matplotlib
- Seaborn

## Dataset
The dataset should be a CSV file named `processed_data.csv`. It should contain several features and a binary target column named `klass`, where 0 represents 'Nonflaky' and 1 represents 'Flaky'.

## Usage
1. **Data Preparation**: Load and shuffle the dataset using Pandas. Split the dataset into features (X) and the target variable (y).

2. **Splitting Data**: The data is split into training, validation, and test sets. 80% of the data is used for training and 20% for testing, which is further split into validation and test sets.

3. **Model Architecture**: The model is a sequential neural network with dense layers and dropout for regularization. It is compiled with the Adam optimizer and binary crossentropy loss function.

4. **Training**: The model is trained with early stopping and learning rate reduction on plateaus to prevent overfitting.

5. **Evaluation**: The model's performance is evaluated on the test set using accuracy and the macro F1 score.

6. **Confusion Matrix**: A confusion matrix is generated to visualize the performance of the model on the test data.

To run the script, ensure all dependencies are installed and execute the Python file containing the script.

## Example Output
The script prints the accuracy and macro F1 score of the model on the test data. It also displays a confusion matrix to show the classification results.
