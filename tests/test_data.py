import pytest
import pandas as pd
import os

def test_data_file_exists():
    """Test that the insurance data file exists."""
    assert os.path.exists('data/raw/insurance_data.txt'), "Insurance data file not found"

def test_data_loading():
    """Test that the insurance data can be loaded."""
    try:
        df = pd.read_csv('data/raw/insurance_data.txt', sep='|')
        assert isinstance(df, pd.DataFrame), "Data should be loaded as a DataFrame"
        assert not df.empty, "DataFrame should not be empty"
    except Exception as e:
        pytest.fail(f"Failed to load data: {str(e)}")

def test_required_columns():
    """Test that required columns are present in the data."""
    df = pd.read_csv('data/raw/insurance_data.txt', sep='|')
    required_columns = ['TotalPremium', 'TotalClaims', 'Province', 'Gender', 'VehicleType']
    for col in required_columns:
        assert col in df.columns, f"Required column {col} not found in data" 