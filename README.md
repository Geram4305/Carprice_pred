# Data

The dataset used in this project contains information on different car models sold in the American market. It includes various independent variables such as car specifications, features, and attributes, along with corresponding prices. The dataset has been collected through extensive market surveys and offers a representative sample of the American car market.

# Approach

In this project, random forest is used as the predictive modeling technique to estimate car prices. The goal is to identify the variables that significantly influence car prices and develop a model that accurately predicts the price based on these variables.Finally,deploy the Model using a web service - Using Flask web framework to deploy our trained model on Heroku

# Methodology

1. Data Exploration: Performed an exploratory analysis of the dataset to gain insights into the distribution of variables, identify missing values, and understand the relationships between variables.
2. Data Preprocessing: This involved transforming variables, handling missing values, if required, and transforming categorical variables to numerical ones-
3. Feature Selection: Mainly used random forests' feature importance to select the most relevant independent variables for predicting car prices.
4. Model Development: Implemented random forest to build a predictive model. The model was trained on a portion of the dataset and evaluated using appropriate performance metrics.
5. Model Evaluation: Assessed the performance of the predictive model using evaluation metrics such as negative mean squared error (NMSE),
6. Model Integration: To make the model accessible and user-friendly,integrated it into a web application using Flask, a Python web framework. The web application allows users to input car specifications and obtain price predictions based on the trained model.
8. Model Deployment: The model, along with the Flask web application, is deployed on a heroku, a cloud platform for easy access.
