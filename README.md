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

### Task 4: Statistical Modeling

- [ ] Linear regression for zip code claim prediction
- [ ] Machine learning models for premium optimization
- [ ] Feature importance analysis with SHAP
- [ ] Model evaluation and comparison

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
