def extract_features(data):
    """
    Extract relevant features from the data.
    
    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        pd.DataFrame: Data with extracted features.
    """
    # Example feature extraction
    features = data[['feature1', 'feature2', 'feature3']]
    return features
