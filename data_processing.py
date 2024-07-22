import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def preprocess_data(data):
    """
    Preprocess the loaded data.
    
    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned and preprocessed data.
    """
    # Example preprocessing steps
    data.fillna(0, inplace=True)
    data['feature'] = data['feature'].astype(float)
    return data
