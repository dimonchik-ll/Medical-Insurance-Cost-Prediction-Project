# Medical Insurance Cost Prediction
Predicts medical insurance charges based on user input using machine learning.

## About the project
This dataset provides a granular look at the personal health data of 1,338 individuals in the United States. It reveals how factors like age, BMI, smoking habits, and family size influence the final annual medical bills charged by health insurance companies. For the sake of this project we will use the charges as a target variable whose values need to be predicted and the rest of the fields will be treated as dependent variables.
Since this is going to be a regression problem, we will use traditional Machine Learning algorithms like Linear Regression, SVR, Decision Tree Regressor. We will perform an analysis of the predictions of each of these algorithms and choose the one that gives us the best metrics after hyper-parameter tuning of the model during training.

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/dimonchik-ll/Medical-Insurance-Cost-Prediction-Project.git
cd Medical-Insurance-Cost-Prediction-Project

### 2. Create and activate virtual environment
Windows
```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run backend (FastAPI)
```bash
uvicorn service:app --reload
```

Backend will be available at:
```bash
http://127.0.0.1:8000
```

### 5. Run frontend (Streamlit)
```bash
streamlit run app.py
```