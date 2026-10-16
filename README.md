# Student Performance Prediction

An end-to-end machine learning project that predicts a student's **math score** from demographic, educational, and assessment-related features. The project demonstrates a structured ML workflow with data ingestion, preprocessing, model comparison, artifact serialization, and a Flask web interface.

## Overview

The model uses these input features:

- Gender
- Race/ethnicity group
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

The target variable is `math_score`. The training code compares several regression algorithms and uses the R² score to evaluate model performance.

## Workflow

1. **Exploratory data analysis** — inspect the student performance dataset in Jupyter notebooks.
2. **Data ingestion** — load `notebook/data/stud.csv`, save a raw copy, and split the data into training and test sets.
3. **Data transformation** — impute missing numerical values, standardize numerical features, impute categorical values, and one-hot encode categorical features.
4. **Model training** — compare regression models, tune selected hyperparameters, evaluate performance, and save the selected model.
5. **Prediction** — load the saved model and preprocessor to transform input features and generate a prediction.
6. **Web application** — use the Flask app and HTML templates to collect inputs and display the predicted math score.

## Project Structure

```text
real-template-setup-workflow/
├── .ebextensions/
│   └── python.config          # AWS Elastic Beanstalk WSGI configuration
├── artifacts/                 # Generated datasets, preprocessor, and model
├── notebook/
│   ├── data/
│   │   └── stud.csv           # Input student performance dataset
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/
│   ├── home.html
│   └── index.html
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

## Tech Stack

- **Python** — project implementation
- **Pandas and NumPy** — data handling
- **Scikit-learn** — preprocessing, model selection, and evaluation
- **CatBoost and XGBoost** — additional regression models
- **Matplotlib and Seaborn** — exploratory data analysis and visualization
- **Flask** — web application
- **Jupyter Notebook** — experimentation
- **AWS Elastic Beanstalk configuration** — deployment configuration

## Getting Started

### Prerequisites

- Python 3.9 or a compatible version for the dependencies
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/nuespringramalimarouane-prog/real-template-setup-workflow.git
cd real-template-setup-workflow
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The requirements file includes `-e .`, which installs the project as an editable package using `setup.py`.

### 4. Prepare the dataset

Ensure the student performance CSV is available at:

```text
notebook/data/stud.csv
```

The ingestion component expects this exact path and the expected student-performance columns.

### 5. Train the model

Run the data ingestion component from the repository root:

```bash
python -m src.components.data_ingestion
```

This runs data ingestion, train/test splitting, preprocessing, and model training. The generated files are written under `artifacts/`, including the preprocessor and trained model.

### 6. Start the web application

After the model and preprocessor artifacts have been generated, run:

```bash
python app.py
```

Open the local address shown in the terminal. The application provides a form for entering student information and displaying the predicted math score.

## Model Evaluation

The training component compares multiple regression algorithms, including:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- K-Neighbors Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

Models are evaluated using the **R² score**. The trainer selects the highest-scoring model and saves it when it meets the configured threshold.

## Notes

- Training and inference depend on the same feature schema and preprocessing pipeline.
- The dataset must be present at the expected path before training.
- The web app requires the generated `artifacts/model.pkl` and `artifacts/preprocessor.pkl` files.
- Review the input-to-feature mapping in `app.py` before relying on predictions: the current form handling appears to pass reading and writing scores in reversed order.
- Model quality depends on the dataset and evaluation results; predictions should not be treated as guarantees of student performance.

## Author

**Marouane** — Computer Science and Big Data student interested in Machine Learning, Data Science, and Software Engineering.

## Repository

[GitHub: real-template-setup-workflow](https://github.com/nuespringramalimarouane-prog/real-template-setup-workflow)
