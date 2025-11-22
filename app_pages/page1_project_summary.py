import streamlit as st

def page1_project_summary_body():
    """
    Page 1: Project Summary
    """
    
    st.markdown("## 📊 Project Summary")
    st.markdown("### Educational ML Tool for Bitcoin Trading Risk Assessment")
    
    st.markdown("---")
    
    # Main warning banner
    st.error("""
    ⚠️ **EDUCATIONAL TOOL ONLY - NOT FOR ACTUAL TRADING**
    
    This system demonstrates realistic limitations of ML in financial markets.
    Both models show weak predictive power:
    - Classification: 51% accuracy (barely above coin flip)
    - Regression: R² = -0.037 (no predictive power)
    
    **Purpose:** Educational demonstration of market efficiency challenges.
    
    Always consult financial professionals and never trade based on ML predictions alone.
    """)
    
    st.markdown("---")
    
    # Project Introduction
    st.markdown("### 🎯 Project Purpose")
    st.info("""
    **TradeCare** aims to help beginner traders understand the challenges of short-term 
    cryptocurrency prediction using machine learning. Rather than providing actionable 
    trading signals, this project demonstrates:
    
    - ✅ Complete data science workflow (CRISP-DM)
    - ✅ Proper ML pipeline implementation
    - ✅ Honest assessment of model limitations
    - ✅ Educational value of negative results
    - ✅ Understanding of market efficiency
    
    **Key Learning:** Short-term price prediction is extremely difficult, even with 
    sophisticated technical indicators and ML models.
    """)
    
    st.markdown("---")
    
    # Business Requirements
    st.markdown("### 📋 Business Requirements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### BR1: Price Movement Prediction")
        st.markdown("""
        **Goal:** Predict 4-hour Bitcoin price change (%)
        
        **Implementation:**
        - Model: Linear Regression
        - Target: Continuous percentage return
        - Features: 14 technical indicators
        
        **Results:**
        - ✅ RMSE: 0.98% (acceptable error)
        - ✅ MAE: 0.66% (acceptable error)
        - ❌ R²: -0.037 (no predictive power)
        
        **Finding:** Model achieves low error but cannot beat baseline. 
        Indicates random walk behavior at 4h timeframe.
        """)
    
    with col2:
        st.markdown("#### BR2: Trade Profitability Assessment")
        st.markdown("""
        **Goal:** Predict if trade will be profitable (binary)
        
        **Implementation:**
        - Model: Logistic Regression
        - Target: Profitable (1) vs Not (0)
        - Features: Same 14 technical indicators
        
        **Results:**
        - ❌ Accuracy: 51.04% (near random 50%)
        - ❌ ROC-AUC: 0.5375 (weak discrimination)
        
        **Finding:** Marginal improvement over coin flip. 
        Directional prediction as difficult as exact values.
        """)
    
    st.markdown("---")
    
    # Dataset Information
    st.markdown("### 📦 Dataset Information")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Source", "Bitcoin OHLCV")
        st.caption("Hourly candlestick data")
    
    with col2:
        st.metric("Timeframe", "2020-2025")
        st.caption("5 years, gap-free")
    
    with col3:
        st.metric("Samples", "~48,000")
        st.caption("After filtering & cleaning")
    
    with col4:
        st.metric("Features", "14")
        st.caption("Technical indicators")
    
    st.markdown("---")
    
    # Feature List
    st.markdown("### 🔧 Features Engineered")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Price Momentum (4)**")
        st.markdown("""
        - return_1h
        - return_4h
        - return_12h
        - return_24h
        """)
    
    with col2:
        st.markdown("**Trend Indicators (7)**")
        st.markdown("""
        - rsi (14-period)
        - ma_10, ma_20, ma_50
        - dist_from_ma10
        - dist_from_ma20
        """)
    
    with col3:
        st.markdown("**Volume & Volatility (3)**")
        st.markdown("""
        - volume_change
        - volume_ratio
        - volatility_24h
        - price_range
        """)
    
    st.markdown("---")
    
    # Key Findings
    st.markdown("### 🔑 Key Findings")
    
    st.warning("""
    **Main Conclusion: Short-term Bitcoin prediction is extremely difficult**
    
    Despite using:
    - ✅ Clean, gap-free data (2020-2025)
    - ✅ 14 engineered technical indicators
    - ✅ Proper time-series methodology
    - ✅ Appropriate model selection
    
    Results show:
    - ❌ Regression R² = -0.037 (worse than baseline)
    - ❌ Classification accuracy = 51% (near random)
    
    **This aligns with efficient market hypothesis:** Short-term prices in liquid 
    markets are difficult to predict.
    """)
    
    st.success("""
    **Scientific Value of Negative Results:**
    
    - ✅ Demonstrates complete CRISP-DM workflow
    - ✅ Shows proper ML pipeline implementation
    - ✅ Provides honest performance assessment
    - ✅ Educates about market efficiency
    - ✅ Confirms academic literature on prediction difficulty
    
    **Negative results are valid and valuable scientific findings!**
    """)
    
    st.markdown("---")
    
    # Project Links
    st.markdown("### 🔗 Project Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Dataset Source:**
        - [Bitcoin Hourly OHLCV Dataset](https://github.com/mouadja02/bitcoin-hourly-ohclv-dataset)
        - Updated daily
        - Public domain
        """)
    
    with col2:
        st.markdown("""
        **Project Documentation:**
        - Complete README with methodology
        - Jupyter notebooks with analysis
        - Model training pipeline
        - Honest performance assessment
        """)
    
    st.markdown("---")
    
    # Navigation hint
    st.info("""
    👉 **Explore the dashboard:**
    - **Data Study:** See correlation analysis and feature insights
    - **Price & Trade Predictor:** Try the live prediction tool (with disclaimers)
    - **Hypothesis Validation:** Review scientific findings
    - **Technical Overview:** Examine detailed model performance
    """)