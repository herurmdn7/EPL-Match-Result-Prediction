# English Premier League Classification Model

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Project Structure](#project-structure)
3. [Installation and Setup](#installation-and-setup)
4. [Data](#data)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Preprocessing](#preprocessing)
7. [Modeling](#modeling)
8. [Evaluation](#evaluation)
9. [Results](#results)
10. [Conclusion](#conclusion)
11. [Future Work](#future-work)
12. [References and Deployment](#references-and-deployment)

---

### 1. Project Overview
This project focuses on predicting the outcome of English Premier League matches based on historical data. The main objective is to classify match results into home win, draw, or away win using machine learning models.

- **Goal**: Build a classification model to predict match outcomes.
- **Dataset**: EPL historical data.
- **Algorithms Used**: SVM, Logistic Regression, etc.
- **Key Findings**: Model evaluation and analysis of misclassified data.

---

### 2. Project Structure
```bash
├── deployment/
│   ├── app.py                     # Streamlit App Page
│   └── eda.py                     # EDA Deployment Page
│   └── prediction.py              # Prediction Deployment Page
│   └── requirements.txt           # Dependencies
│   └── model.pkl                  # Saved model files
│   └── P1M2_Heru.csv              # Raw Data for Streamlit
│   └── cc1.jpg                    # Image for Deployment
├── P1M2_Heru.csv                  # Raw Data
├── P1M2_Heru.ipynb                # Notebooks
├── P1M2_Heru_Inf.ipynb            # Inference Notebooks
├── README.md                      # This README file
├── model.pkl                      # Saved model files
└── url.txt                        # Dataset and Deplotment url
```

---

### 3. Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/herurmdn7/EPL-Match-Result-Prediction.git
   ```
2. Install required packages:
   ```bash
   pip install -r deployment/requirements.txt
   ```
3. Ensure the correct version of Python (>=3.7) is installed.

---

### 4. Data
- **Source**: English Premier League dataset.
- **Structure**: The dataset consists of 18 columns with match details and outcomes.
- **Missing Data**: The dataset contains missing values in some columns, primarily in the 1993-2000 seasons.

---

### 5. Exploratory Data Analysis (EDA)
- **Analysis**: Explored trends and patterns in the data, including:
  - Match outcome distribution
  - Home vs. away performance
  - Impact of halftime results on match outcomes
- **Visualization**: Various heatmaps and bar charts used to visualize missing values and class distributions.

---

### 6. Preprocessing
- **Handling Missing Values**: Filtered and filled missing data.
- **Data Filtering**: Season-specific filtering applied to remove years with excessive missing data (1993-2000).
- **Cardinality Test**: Tested for high cardinality columns and removed them where necessary.
- **Outlier Handling**: Handled outliers using Winsorization.
- **Data Capping**: Applied data capping techniques to handle extreme values.
- **Column Correlations to Target**: Used chi-squared test for nominal data and Spearman correlation for numerical data to check correlation with the target variable.


---

### 7. Modeling
- **Algorithms**: Models used include:
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Random Forest
- **Cross-Validation**: Applied 5-fold cross-validation for model evaluation.
- **Pipelines**: Used a pipeline for preprocessing and model training.
- **Hyperparameter Tuning**:
  - **SVM**: Tuned using RandomizedSearchCV for optimal parameters such as kernel, C, and gamma.
  - **KNN**: Tuned using RandomizedSearchCV for optimal parameters such as the number of neighbors (k) and distance metrics.
- **Boosting and Bagging**:
  - Applied **AdaBoostClassifier** to enhance SVM performance.
  - Applied **BaggingClassifier** to improve KNN robustness and reduce variance.


---

### 8. Evaluation
- **Metrics**: Accuracy, F1-score, confusion matrix.
- **Key Findings**: The SVM model performed the best with an F1-score of 0.99 on the test set.
- **Error Analysis**: Investigated false negatives and positives for both home wins and away wins.

---

### 9. Results
- **Best Model**: SVM with 0.99 F1 score.
- **Misclassification Patterns**: False negatives and positives were identified for matches with tight score differences.
- **Insights**: Home teams tend to perform significantly better, impacting prediction accuracy.

---

### 10. Conclusion
This classification project demonstrates the ability to predict EPL match outcomes with high accuracy. Further improvements could involve using additional data sources such as player stats or live odds.

---

### 11. Future Work
- **Data Augmentation**: Incorporate more detailed player and match data.

---

### 12. References and Deployment
- English Premier League dataset: [Kaggle EPL Dataset](https://www.kaggle.com/datasets/irkaal/english-premier-league-results)
- Huggingface: [Deployment](https://huggingface.co/spaces/Flickerjet/EPL_Result_Prediction)
