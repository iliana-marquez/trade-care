import streamlit as st
import joblib
import os

@st.cache_resource
def load_models():
    """
    Load trained models, scaler, and feature names
    
    Returns:
        tuple: (regression_model, classification_model, scaler, feature_names)
    """
    try:
        # Define paths
        models_dir = 'outputs/models'
        
        regression_path = os.path.join(models_dir, 'regression_model.pkl')
        classification_path = os.path.join(models_dir, 'classification_model.pkl')
        scaler_path = os.path.join(models_dir, 'scaler.pkl')
        features_path = os.path.join(models_dir, 'feature_names.pkl')
        
        # Check if files exist
        if not all([
            os.path.exists(regression_path),
            os.path.exists(classification_path),
            os.path.exists(scaler_path),
            os.path.exists(features_path)
        ]):
            st.error("❌ Model files not found in outputs/models/")
            return None, None, None, None
        
        # Load models
        regression_model = joblib.load(regression_path)
        classification_model = joblib.load(classification_path)
        scaler = joblib.load(scaler_path)
        feature_names = joblib.load(features_path)
        
        return regression_model, classification_model, scaler, feature_names
        
    except Exception as e:
        st.error(f"❌ Error loading models: {str(e)}")
        return None, None, None, None