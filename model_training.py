from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(features, labels):
    """
    Train a machine learning model.
    
    Args:
        features (pd.DataFrame): Extracted features.
        labels (pd.Series): Target labels.

    Returns:
        RandomForestClassifier: Trained model.
    """
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/trained_model.pkl')
    return model
