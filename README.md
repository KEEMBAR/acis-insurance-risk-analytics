# ACIS Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project is part of the AlphaCare Insurance Solutions (ACIS) marketing and risk analytics challenge. The goal is to analyze historical insurance claim data to optimize marketing strategy and discover "low-risk" targets for premium reduction, creating opportunities to attract new clients.

## Business Objective

- Analyze historical insurance claim data from Feb 2014 to Aug 2015
- Optimize marketing strategy for car insurance in South Africa
- Discover low-risk segments for premium reduction
- Build predictive models for risk assessment and premium optimization

## Project Structure

```
acis-insurance-risk-analytics/
├── data/                   # Data files (version controlled with DVC)
│   ├── raw/               # Original insurance data
│   ├── processed/         # Cleaned and processed data
│   └── external/          # External data sources
├── src/                   # Source code
│   ├── data/             # Data processing scripts
│   ├── features/         # Feature engineering
│   ├── models/           # Model training and evaluation
│   └── visualization/    # Plotting and visualization
├── notebooks/            # Jupyter notebooks for analysis
├── reports/              # Generated reports and visualizations
├── models/               # Saved model files
├── tests/                # Unit tests
└── docs/                 # Documentation
```

## Tasks Overview

### Task 1: Git, GitHub & EDA

- [x] Git repository setup with proper branching
- [x] CI/CD with GitHub Actions
- [x] Exploratory Data Analysis (EDA)
- [x] Statistical analysis and insights

### Task 2: Data Version Control (DVC)

- [ ] DVC installation and setup
- [ ] Local remote storage configuration
- [ ] Data versioning and tracking

### Task 3: A/B Hypothesis Testing

- [ ] Risk differences across provinces
- [ ] Risk differences between zip codes
- [ ] Margin differences between zip codes
- [ ] Risk differences between genders

### Task 4: Predictive Modeling & Model Interpretation

### Overview

In Task 4, we built and evaluated several regression models (Linear Regression, Random Forest, XGBoost) to predict claim severity for car insurance policies. We also used SHAP to interpret model predictions and identify the most influential features.

### Steps Performed

- Data cleaning and feature engineering
- Train-test split
- Model training and evaluation (Linear Regression, Random Forest, XGBoost)
- Model comparison using RMSE and R²
- Model interpretation using SHAP
- Business recommendations based on model results and feature importance

### Key Findings

- All models performed poorly (low or negative R²), indicating claim severity is difficult to predict with the current data.
- SHAP analysis showed CalculatedPremiumPerTerm and SumInsured as the most influential features, but overall predictive power was low.

### Recommendations

- Consider collecting more granular or additional data.
- Explore alternative modeling targets, such as claim frequency (classification).
- Use domain knowledge to engineer new features that may improve model performance.

## Modular Code Organization (`src/`)

Reusable code for feature engineering, model training, and evaluation is organized in the `src/` directory:

- `src/features/feature_engineering.py`: Feature creation functions
- `src/features/feature_selection.py`: Feature selection utilities
- `src/models/train.py`: Model training functions
- `src/models/evaluate.py`: Model evaluation metrics
- `src/models/predict.py`: Model prediction functions

**How to use in your notebook:**

```python
from src.features.feature_engineering import add_vehicle_age
from src/models.train import train_linear_regression
from src/models/evaluate import evaluate_regression
```

This structure keeps the project modular, maintainable, and ready for future development.

## Key Metrics

- **Loss Ratio**: TotalClaims / TotalPremium
- **Claim Frequency**: Proportion of policies with claims
- **Claim Severity**: Average claim amount given a claim occurred
- **Margin**: TotalPremium - TotalClaims

## Data Schema

The dataset includes information about:

- **Policy**: UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client**: Gender, MaritalStatus, Citizenship, etc.
- **Location**: Country, Province, PostalCode, CrestaZones
- **Vehicle**: Make, Model, Year, Type, Value, etc.
- **Coverage**: SumInsured, Premium, Excess, CoverType
- **Claims**: TotalPremium, TotalClaims

## Setup Instructions

### Prerequisites

- Python 3.8+
- Git
- DVC

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd acis-insurance-risk-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize DVC
dvc init
dvc remote add -d localstorage ./data/dvc_storage
```

### Usage

```bash
# Run EDA
python src/data/exploratory_analysis.py

# Run hypothesis testing
python src/models/hypothesis_testing.py

# Train models
python src/models/train_models.py
```

## Data Version Control (DVC)

This project uses [DVC](https://dvc.org/) to manage large data files and ensure reproducibility and auditability of all analyses and models. DVC allows us to:

- Version control large datasets without bloating the Git repository
- Reproduce any analysis or model result at any time
- Share data efficiently with collaborators

### How DVC Works in This Project

- The actual data files (e.g., `insurance_data.txt`) are **not** tracked by Git, but by DVC.
- Only small `.dvc` files (e.g., `insurance_data.txt.dvc`) and DVC config files are tracked by Git.
- The data itself is stored in a local DVC remote (`data/dvc_storage/`).
- When you clone the repo, you get the code and `.dvc` files. To get the data, you run `dvc pull`.

### How to Get the Data

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```
2. **Install DVC:**
   ```bash
   pip install dvc
   ```
3. **Pull the data:**
   ```bash
   dvc pull
   ```
   This will download the required data files into the correct locations from the DVC remote storage.

### How to Add or Update Data (for contributors)

1. Place new or updated data files in the appropriate `data/` subdirectory.
2. Track the file with DVC:
   ```bash
   dvc add data/raw/your_new_data.csv
   ```
3. Commit the `.dvc` file and DVC config changes to Git:
   ```bash
   git add data/raw/your_new_data.csv.dvc data/raw/.gitignore .dvc/config
   git commit -m "Track new data file with DVC"
   ```
4. Push the data to the DVC remote:
   ```bash
   dvc push
   ```

### Troubleshooting

- If you see an error about a file being git-ignored, make sure your `.gitignore` allows `.dvc` files but not the actual data files.
- If `dvc pull` fails, check your DVC remote configuration and storage permissions.

**Note:** The actual data files are not tracked by Git, only by DVC. The `.dvc` files are tracked by Git and ensure data versioning and reproducibility.
