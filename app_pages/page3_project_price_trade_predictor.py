import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_models

def page3_project_price_trade_predictor_body():
    """
    Page 3: Live Price & Trade Predictor
    """
    
    st.markdown("## 🎯 Price & Trade Predictor")
    
    # Warning banner
    st.error("""
    ⚠️ **CRITICAL LIMITATIONS - READ BEFORE USE**
    
    **Model Performance:**
    - Regression R² = -0.037 (NO predictive power)
    - Classification Accuracy = 51% (near coin flip)
    
    **This tool is for EDUCATIONAL demonstration only.**
    
    Predictions have **no statistical reliability** and should **NEVER** 
    be used for actual trading decisions.
    """)
    
    st.markdown("---")
    
    # Load models
    reg_model, clf_model, scaler, feature_names = load_models()
    
    if reg_model is None:
        st.error("❌ Models not loaded. Please ensure model files exist in outputs/models/")
        st.stop()
    
    # Instructions
    st.markdown("### 📊 How to Use This Tool")
    st.info("""
    1. **Input current Bitcoin market conditions** using sliders below
    2. **Click "Get Predictions"** to generate forecasts
    3. **Review both predictions:**
       - **BR1 (Regression):** Expected price change %
       - **BR2 (Classification):** Probability of profitability
    4. **Remember:** Predictions have minimal reliability (see warnings)
    
    **Data Sources:** Check TradingView, CoinMarketCap, or similar platforms 
    for current Bitcoin indicators before inputting values.
    """)
    
    st.markdown("---")
    
    # Input form
    st.markdown("### 📝 Input Market Conditions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📈 Price Returns**")
        return_1h = st.slider("1-Hour Return (%)", -10.0, 10.0, 0.0, 0.1, 
                              help="Price change over last 1 hour")
        return_4h = st.slider("4-Hour Return (%)", -20.0, 20.0, 0.0, 0.1,
                              help="Price change over last 4 hours")
        return_12h = st.slider("12-Hour Return (%)", -30.0, 30.0, 0.0, 0.1,
                               help="Price change over last 12 hours")
        return_24h = st.slider("24-Hour Return (%)", -40.0, 40.0, 0.0, 0.1,
                               help="Price change over last 24 hours")
    
    with col2:
        st.markdown("**📊 Technical Indicators**")
        rsi = st.slider("RSI (14-period)", 0.0, 100.0, 50.0, 0.5,
                       help="Relative Strength Index: <30 oversold, >70 overbought")
        
        st.markdown("**Moving Averages**")
        current_price = st.number_input("Current BTC Price ($)", 
                                        min_value=1000, max_value=150000, 
                                        value=50000, step=100)
        ma_10 = st.number_input("10-Period MA ($)", 
                                min_value=1000, max_value=150000, 
                                value=49500, step=100)
        ma_20 = st.number_input("20-Period MA ($)", 
                                min_value=1000, max_value=150000, 
                                value=49000, step=100)
        ma_50 = st.number_input("50-Period MA ($)", 
                                min_value=1000, max_value=150000, 
                                value=48000, step=100)
    
    with col3:
        st.markdown("**💹 Volume & Volatility**")
        volume_change = st.slider("Volume Change (%)", -100.0, 200.0, 0.0, 1.0,
                                  help="Percentage change in trading volume")
        volume_ratio = st.slider("Volume Ratio", 0.1, 5.0, 1.0, 0.1,
                                 help="Current volume vs 10-period average")
        volatility_24h = st.slider("24h Volatility", 0.0, 0.1, 0.02, 0.001,
                                   help="Standard deviation of 1h returns over 24h")
        price_range = st.slider("Price Range (H-L/Close)", 0.0, 0.1, 0.02, 0.001,
                                help="High-Low spread normalized by close")
        
        st.markdown("---")
        st.markdown("**📏 Auto-Calculated**")
        dist_from_ma10 = ((current_price - ma_10) / ma_10) * 100
        dist_from_ma20 = ((current_price - ma_20) / ma_20) * 100
        st.metric("Distance from MA10", f"{dist_from_ma10:+.2f}%")
        st.metric("Distance from MA20", f"{dist_from_ma20:+.2f}%")
    
    st.markdown("---")
    
    # Predict button
    if st.button("🔮 Get Predictions", type="primary", use_container_width=True):
        
        # Prepare features (convert to decimals)
        features = np.array([[
            return_1h / 100,
            return_4h / 100,
            return_12h / 100,
            return_24h / 100,
            rsi,
            ma_10,
            ma_20,
            ma_50,
            dist_from_ma10 / 100,
            dist_from_ma20 / 100,
            volume_change / 100,
            volume_ratio,
            volatility_24h,
            price_range
        ]])
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make predictions
        reg_prediction = reg_model.predict(features_scaled)[0]
        clf_prediction = clf_model.predict(features_scaled)[0]
        clf_probability = clf_model.predict_proba(features_scaled)[0][1]
        
        st.markdown("---")
        st.markdown("## 🎯 Prediction Results")
        
        # Display predictions
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 BR1: Price Movement Prediction")
            st.markdown("**4-Hour Expected Price Change:**")
            
            # Color based on direction
            if reg_prediction > 0:
                st.success(f"### +{reg_prediction*100:.2f}%")
                st.caption("🟢 Predicted to rise")
            else:
                st.error(f"### {reg_prediction*100:.2f}%")
                st.caption("🔴 Predicted to fall")
            
            # Expected price
            expected_price = current_price * (1 + reg_prediction)
            st.metric("Expected Price (4h)", f"${expected_price:,.0f}",
                     delta=f"{reg_prediction*100:+.2f}%")
            
            st.markdown("---")
            st.warning("""
            ⚠️ **Model Limitations:**
            - R² Score: -0.037
            - RMSE: 0.98%
            - **No predictive power**
            
            This prediction is essentially random.
            """)
        
        with col2:
            st.markdown("### 🎯 BR2: Trade Profitability Prediction")
            st.markdown("**Probability of Profitable Trade:**")
            
            # Display probability
            st.metric("Profitability Probability", f"{clf_probability*100:.1f}%")
            
            # Risk assessment
            if clf_probability > 0.65:
                risk_level = "Low Risk"
                risk_color = "🟢"
                risk_msg = "success"
            elif clf_probability < 0.40:
                risk_level = "High Risk"
                risk_color = "🔴"
                risk_msg = "error"
            else:
                risk_level = "Medium Risk"
                risk_color = "🟡"
                risk_msg = "warning"
            
            if risk_msg == "success":
                st.success(f"{risk_color} **Risk Level:** {risk_level}")
            elif risk_msg == "error":
                st.error(f"{risk_color} **Risk Level:** {risk_level}")
            else:
                st.warning(f"{risk_color} **Risk Level:** {risk_level}")
            
            # Binary prediction
            if clf_prediction == 1:
                st.info("📈 **Model suggests:** Likely profitable")
            else:
                st.info("📉 **Model suggests:** Likely not profitable")
            
            st.markdown("---")
            st.warning("""
            ⚠️ **Model Limitations:**
            - Accuracy: 51.04%
            - ROC-AUC: 0.5375
            - **Barely better than random**
            
            This is essentially a coin flip.
            """)
        
        st.markdown("---")
        
        # Feature importance display
        st.markdown("### 📈 Feature Influence Analysis")
        st.caption("Top features that influenced this prediction:")
        
        # Create feature importance table
        feature_data = {
            'Feature': ['4h Return', '12h Return', '1h Return', 'Dist from MA10', 'RSI'],
            'Your Input': [
                f"{return_4h:+.2f}%",
                f"{return_12h:+.2f}%",
                f"{return_1h:+.2f}%",
                f"{dist_from_ma10:+.2f}%",
                f"{rsi:.1f}"
            ],
            'Interpretation': [
                '🟢 Bullish' if return_4h > 0 else '🔴 Bearish',
                '🟢 Uptrend' if return_12h > 0 else '🔴 Downtrend',
                '🟢 Rising' if return_1h > 0 else '🔴 Falling',
                '🟢 Above MA' if dist_from_ma10 > 0 else '🔴 Below MA',
                '🔴 Overbought' if rsi > 70 else ('🟢 Oversold' if rsi < 30 else '🟡 Neutral')
            ]
        }
        
        feature_df = pd.DataFrame(feature_data)
        st.table(feature_df)
        
        st.info("""
        **Remember:** Even these "influential" features have weak correlations (<0.35). 
        The model's overall performance is near-random, so do not make trading decisions 
        based on these predictions.
        """)
        
        st.markdown("---")
        
        # Final disclaimer
        st.error("""
        ### ⚠️ FINAL REMINDER
        
        **DO NOT USE FOR ACTUAL TRADING:**
        
        - ❌ Model has no statistical reliability
        - ❌ Predictions are near-random (51% accuracy, R²=-0.037)
        - ❌ Markets are more complex than 14 technical indicators
        - ❌ Short-term prediction is extremely difficult
        
        **FOR EDUCATIONAL PURPOSES ONLY**
        
        This tool demonstrates why beginners should:
        - Focus on risk management over prediction
        - Use multiple information sources
        - Avoid over-reliance on any single model
        - Practice proper position sizing
        - Consult financial professionals
        """)
    
    else:
        # Show helper message when button not clicked
        st.info("""
        👆 **Adjust the sliders above** to match current Bitcoin market conditions, 
        then click "Get Predictions" to see model outputs.
        
        **Tip:** Get current values from TradingView, CoinMarketCap, or your 
        preferred crypto data source.
        """)