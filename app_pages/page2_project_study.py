import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page2_project_study_body():
    """
    Page 2: Data Study & Correlation Analysis
    """
    
    st.markdown("## 📈 Data Study & Feature Analysis")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("### 🔍 Correlation Study Overview")
    st.info("""
    This page shows which features correlate with trade profitability.
    
    **Purpose:** Understand which technical indicators have the strongest relationship 
    with profitable trades (supports both BR1 and BR2).
    
    **Note:** Even the strongest correlations are weak (<0.4), explaining why 
    models have limited predictive power.
    """)
    
    st.markdown("---")
    
    # Feature correlation data (from notebook results)
    st.markdown("### 📊 Feature Correlation with Profitability")
    
    # Create correlation data
    correlation_data = {
        'Feature': [
            'return_4h',
            'return_12h',
            'return_1h',
            'return_24h',
            'dist_from_ma10',
            'dist_from_ma20',
            'volume_ratio',
            'rsi',
            'volatility_24h',
            'volume_change',
            'price_range',
            'ma_10',
            'ma_20',
            'ma_50'
        ],
        'Correlation': [
            0.32, 0.28, 0.25, 0.22,
            0.18, 0.16, 0.08, -0.02,
            -0.05, 0.03, -0.04, 0.01,
            0.02, 0.01
        ],
        'Interpretation': [
            'Recent upward momentum → more likely profitable',
            'Medium-term trend continuation',
            'Short-term momentum signal',
            'Daily trend alignment',
            'Price above short-term MA → bullish',
            'Price above medium-term MA → trend strength',
            'Volume surge → conviction',
            'Neutral (RSI at extremes may reverse)',
            'High volatility → unpredictable',
            'Volume changes weakly predictive',
            'Intrabar volatility low signal',
            'Absolute MA values not predictive',
            'Absolute MA values not predictive',
            'Absolute MA values not predictive'
        ]
    }
    
    corr_df = pd.DataFrame(correlation_data)
    
    # Bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = ['green' if x > 0 else 'red' for x in corr_df['Correlation']]
    ax.barh(corr_df['Feature'], corr_df['Correlation'], color=colors, alpha=0.7)
    ax.axvline(x=0, color='black', linestyle='--', linewidth=1)
    ax.set_xlabel('Correlation with Profitability', fontsize=12)
    ax.set_title('Feature Correlation Analysis', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")
    
    # Correlation table
    st.markdown("### 📋 Detailed Correlation Table")
    st.dataframe(
        corr_df.style.background_gradient(subset=['Correlation'], cmap='RdYlGn', vmin=-0.4, vmax=0.4),
        use_container_width=True
    )
    
    st.markdown("---")
    
    # Key insights
    st.markdown("### 🔑 Key Insights from Correlation Study")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Strongest Predictors")
        st.success("""
        **Momentum Features (Positive Correlation):**
        - `return_4h` (+0.32): Recent 4h trend
        - `return_12h` (+0.28): Medium-term momentum
        - `return_1h` (+0.25): Short-term movement
        
        **Interpretation:** Recent upward momentum weakly predicts 
        continued profitability.
        
        **However:** Correlations <0.4 are considered weak in finance.
        """)
    
    with col2:
        st.markdown("#### Weakest Predictors")
        st.warning("""
        **Low/Negative Correlation:**
        - `volatility_24h` (-0.05): Volatility unclear signal
        - `rsi` (-0.02): Oscillator not predictive
        - Absolute MA values: Not directionally predictive
        
        **Interpretation:** These features add little predictive value 
        at 4h timeframe.
        
        **Note:** Even "strong" correlations are weak overall.
        """)
    
    st.markdown("---")
    
    # Statistical significance
    st.markdown("### 📊 Correlation Strength Interpretation")
    
    st.markdown("""
    **Standard interpretation in financial markets:**
    
    | Correlation | Strength | Predictive Value |
    |-------------|----------|------------------|
    | > 0.7 | Very Strong | High |
    | 0.5 - 0.7 | Strong | Moderate-High |
    | 0.3 - 0.5 | Moderate | Some value |
    | 0.1 - 0.3 | Weak | Minimal value |
    | < 0.1 | Very Weak | No practical value |
    
    **Our results:** Maximum correlation = 0.32 (Weak-to-Moderate)
    
    **Conclusion:** Technical indicators show weak correlations, explaining 
    why both models (regression and classification) have limited predictive power.
    """)
    
    st.markdown("---")
    
    # Connection to hypotheses
    st.markdown("### 🔬 Connection to Project Hypotheses")
    
    st.info("""
    **H1: Technical indicators predict price movement**
    - Result: Correlations exist but weak (<0.35)
    - Regression R² = -0.037 confirms weak prediction
    - **Status: NOT VALIDATED**
    
    **H2: Technical indicators predict profitability**
    - Result: Weak correlations with binary outcome
    - Classification accuracy = 51% confirms minimal prediction
    - **Status: NOT VALIDATED**
    
    **Both hypotheses show consistent findings:** Technical indicators alone 
    have limited predictive power at 4-hour timeframes.
    """)
    
    st.markdown("---")
    
    # Feature groups analysis
    st.markdown("### 🎯 Feature Group Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Momentum Features")
        st.metric("Avg Correlation", "+0.27")
        st.caption("Strongest group (returns)")
        st.markdown("""
        **Features:**
        - return_1h, 4h, 12h, 24h
        
        **Finding:** Recent price momentum 
        shows weak positive correlation.
        """)
    
    with col2:
        st.markdown("#### Trend Features")
        st.metric("Avg Correlation", "+0.06")
        st.caption("Weak predictive value")
        st.markdown("""
        **Features:**
        - MA distances, RSI
        
        **Finding:** Trend indicators 
        minimally predictive at 4h scale.
        """)
    
    with col3:
        st.markdown("#### Volume/Volatility")
        st.metric("Avg Correlation", "+0.01")
        st.caption("No predictive value")
        st.markdown("""
        **Features:**
        - Volume, volatility
        
        **Finding:** Volume and volatility 
        show no useful signal.
        """)
    
    st.markdown("---")
    
    # Implications
    st.markdown("### 💡 Practical Implications")
    
    st.warning("""
    **What this means for traders:**
    
    1. **Technical indicators alone are insufficient** for 4-hour Bitcoin prediction
    2. **Recent momentum is best signal** but still weak (<0.35 correlation)
    3. **No single indicator dominates** - all show weak correlations
    4. **Directional prediction is hard** - 51% accuracy near random
    5. **Market efficiency confirmed** - short-term prices difficult to predict
    
    **Recommendation:** Focus on risk management rather than prediction confidence.
    Use technical indicators as context, not as sole decision drivers.
    """)
    
    st.markdown("---")
    
    # Dataset quality note
    st.markdown("### ✅ Data Quality Note")
    
    st.success("""
    **Dataset Quality:** High
    
    - ✅ 95.4% retention after cleaning
    - ✅ Zero time gaps (2020-2025)
    - ✅ Validated against historical events
    - ✅ Proper OHLCV logic enforced
    
    **Conclusion:** Weak correlations are NOT due to data quality issues.
    The challenge is inherent to short-term prediction.
    """)