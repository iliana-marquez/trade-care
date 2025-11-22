# Trade Care: Predictive Analytics for Safer Trading Decisions

Welcome to **TradeCare** 👋

An intelligent trading companion designed to help beginner traders make safer, data-driven decisions.

Many new traders lose money by following emotions, social-media hype from “investor influencers,” or falling for scam brokers. TradeCare protects you with:
- Price movement predictions based on machine learning
- Profitability probability scores for potential trades
- Risk assessments that warn you before losses happen

**Our Goals**
- **Minimise Losses:** Understand risk before entering any trade
- **Build Confidence:** Make decisions backed by real data
- **Develop Skills:** Learn what drives successful trades through clear insights
- **Stay Safe:** Avoid impulsive trading and misleading advice 

> [!WARNING]  
> **Important Disclaimer:** TradeCare is an educational tool for risk awareness and decision support. It does not provide financial advice and should not be used as the sole basis for trading decisions.

## Dataset Content

TradeCare uses publicly available cryptocurrency market data (OHLCV - Open, High, Low, Close, Volume) for Bitcoin (BTC-USD) with 1-hour candle intervals.

**Source:** GitHub - Bitcoin Hourly OHLCV Dataset 
**Repository:** https://github.com/mouadja02/bitcoin-hourly-ohclv-dataset  
**Direct File:** btc-hourly-price_2015_2025.csv 
**Asset:** BTC-USD (Bitcoin to US Dollar)  
**Timeframe:** 1-hour candlesticks  
**Period:** December 2014 - November 2025
**Total Records:** depend on the data by the time the notebooks are run

## Data Structure
The dataset contains the following raw columns:

| Column | Data Type | Description | Example (1st Entry) |
|--------|-----------|-------------|---------|
| `TIME_UNIX` | integer | Unix timestamp for the hour | 1416031200 |
| `DATE_STR` | string | Human-readable date (YYYY-MM-DD) | 2014-11-15 |
| `HOUR_STR` | string | Hour of the day | 6 |
| `OPEN_PRICE` | float | Opening price at hour start (USD) | 395.88 |
| `HIGH_PRICE` | float | Highest price during the hour (USD) | 398.12|
| `CLOSE_PRICE` | float | Closing price at hour end (USD) | 396.15
| `LOW_PRICE` | float | Lowest price during the hour (USD) | 394.43 |
| `VOLUME_FROM` | float | Trading volume in BTC | 459.6 |
| `VOLUME_TO` | float | Trading volume in USD | 182309.81| |

**Why This Dataset:**
This dataset is ideal for building the first version of TradeCare’s Bitcoin price-prediction and trade-risk assessment model. It offers the right balance of data quality, volume, and market relevance for a fast-timeline MVP.

- **High Liquidity & 24/7 Trading**: Bitcoin trades continuously across global markets, providing dense and uninterrupted price data. This ensures the model learns from a complete, non-gapped time series.
- **Public, Unbiased Market Data:** Using public OHLCV data avoids the behavioral and statistical bias that exists in individual trader logs. Market-wide data reflects real price formation, liquidity shifts, and volatility conditions.
- **Volatility Suitable for Predictive Modeling:** Bitcoin shows significant short-term volatility as well as mid-term momentum trends. This combination creates enough signal for a model to learn meaningful relationships while still challenging it to generalize.
- **Cycles & Structural Market Patterns:** Contains cyclical and structural patterns that allow the model to capture both short-term dynamics and long-term trends:
    - Halving cycles (every ~4 years)
    - Bull/bear market transitions
    - Volatility clustering
    - Institutional regime shifts (e.g., 2024 ETF approval)
- **Clean, Well-Structured Time-Series Format:**: The dataset contains hourly OHLCV candles in a structured, machine-learning-friendly form. This reduces preprocessing time and makes the pipeline easier to maintain and extend.


## Business Requirements

### **1. Price Movement Prediction**
The client needs to predict short-term Bitcoin price direction before entering a trade

**Implementation:**
- Requires a regression model to predict percentage price change over the next 4 hours
- Visual representation of predicted vs actual price movements with confidence 

**Benefit:** Helps traders set realistic take-profit and stop-loss levels based on expected price movement

### **2. Trade Profitability Assessment**
The client needs to evaluate whether a potential trade setup is likely to be profitable

**Implementation:**
- Requires a classification model to estimate probability of profit
- Risk scoring system categorizing trades as Profitable/Non-Profitable
- Explanation of factors influencing each prediction

**Benefit:** Helps traders set realistic take-profit and stop-loss levels based on expected price movement

## Hypothesis and Validation

### **1. Price Predictability from Technical Indicators**
Current market technical indicators (RSI, moving averages, volatility, volume) contain sufficient signal to predict 4-hour Bitcoin price movements with better-than-random accuracy.

**Validation:**
- Train regression model on historical data (2014-2025)
- Compare model RMSE and MAE against naive baseline (last price carried forward)
- Success criteria: RMSE < 2%, MAE < 1.5%
- Visualize prediction vs actual with scatter plot and residual analysis

### **2. Profitability Classification from Market Conditions**
Technical feature combinations (RSI levels, trend alignment, volatility, volume) can effectively classify whether a trade would be profitable.

**Validation:**
- Train classification model on historical trades (simulated from price data)
- Measure ROC-AUC score (target > 0.60 to show predictive value above random)
- Analyze feature importance to identify key contributors
- Evaluate confusion matrix and precision/recall balance



## The rationale to map the business requirements to the Data Visualizations and ML tasks

### BR1: Price Movement Prediction → Regression Model + Scatter Plot

**Business Requirement:**
Predict 4-hour Bitcoin price movement percentage to help traders set stop-loss and take-profit levels.

**Mapped ML Task:**
* **Type:** Supervised Learning - Regression
* **Model:** Linear Regression
* **Target:** `target_return_simple` (continuous percentage change)
* **Features:** 14 technical indicators (momentum, trend, volume, volatility)

**Data Visualizations:**
* **Scatter Plot (Predicted vs Actual):** Shows model's ability to predict returns
  - Perfect predictions lie on diagonal line
  - Scatter pattern reveals prediction accuracy
  - Separate plots for train/test sets show generalization
* **Correlation Heatmap:** Identifies which features correlate with price returns
  - Guides feature selection
  - Validates relevance of technical indicators
  - Supports hypothesis testing

**Rationale:**
Regression is appropriate because the output is continuous (percentage change can be any value from -20% to +20%). Scatter plots effectively communicate prediction quality to both technical and non-technical stakeholders. The visualization immediately shows whether the model can predict better than random guessing.

---

### BR2: Trade Profitability Assessment → Classification Model + Confusion Matrix

**Business Requirement:**
Predict whether a trade setup will be profitable (binary yes/no) to support beginner decision-making.

**Mapped ML Task:**
* **Type:** Supervised Learning - Binary Classification
* **Model:** Logistic Regression
* **Target:** `target_profitable` (0 = not profitable, 1 = profitable)
* **Features:** Same 14 technical indicators

**Data Visualizations:**
* **Confusion Matrix:** Shows true positives, false positives, true negatives, false negatives
  - Reveals if model is biased toward one class
  - Identifies type of errors being made
  - Essential for imbalanced datasets
* **ROC Curve + AUC Score:** Evaluates classifier performance across thresholds
  - AUC > 0.5 indicates better than random
  - Visual comparison against baseline (random classifier)
  - Standard metric in binary classification
* **Feature Correlation Bar Chart:** Shows which features predict profitability
  - Supports both BR1 and BR2
  - Educational value for users understanding technical indicators

**Rationale:**
Classification simplifies the complex prediction problem into actionable yes/no decision. Confusion matrix and ROC curve are industry-standard visualizations that allow honest assessment of model performance. These visualizations clearly show the 51% accuracy result and near-random performance, providing educational value about prediction difficulty.

---

### Supporting Visualizations

**Feature Engineering Phase:**
* **Return Statistics:** Validates that calculated returns match Bitcoin's volatility patterns
* **RSI Distribution:** Confirms indicator oscillates between 0-100 as expected
* **Moving Average Trends:** Shows trend-following behavior of MA indicators
* **Volume Spike Detection:** Identifies unusual trading activity

**Data Cleaning Phase:**
* **OHLC Validation Charts:** Confirms price logic (High ≥ Low, etc.)
* **Time Gap Analysis:** Identifies continuous vs fragmented data periods
* **Historical Event Verification:** Validates data accuracy against known Bitcoin events

**Rationale:**
These visualizations ensure data quality and feature correctness before model training. They provide evidence of rigorous data preparation and support reproducibility.

---

## ML Business Case

### Business Case 1: Price Movement Prediction (Regression)

#### 1. Business Objectives
**Primary Goal:** Provide beginner traders with estimated 4-hour price movement to inform stop-loss and take-profit placement.

**Target Audience:** 
* Novice cryptocurrency traders lacking risk management experience
* Users seeking data-driven guidance instead of emotional decision-making
* Educational users learning about ML limitations in financial markets

**Business Value:**
* Reduces uninformed trading decisions
* Provides realistic expectations about prediction difficulty
* Educational tool demonstrating market efficiency

#### 2. Problem Definition
**Current Situation:** Beginner traders often enter positions without understanding likely price movement, leading to poorly placed stop-losses and unrealistic profit targets.

**Desired Outcome:** ML system predicts percentage price change over next 4 hours, allowing traders to set appropriate risk parameters.

**Success Criteria:**
* RMSE < 2% (acceptable prediction error)
* MAE < 1.5% (acceptable average error)  
* R² > 0.3 (explains >30% of variance)

**Actual Performance:**
* RMSE: 0.98% ✓ (acceptable)
* MAE: 0.66% ✓ (acceptable)
* R²: -0.037 ✗ (no predictive power)

#### 3. Learning Method
**Supervised Learning - Regression**
* Input: 14 engineered features from OHLCV data
* Output: Continuous value (percentage return)
* Algorithm: Linear Regression (baseline model)
* Training approach: Time-series split (80/20 train/test)

**Why This Method:**
* Simple, interpretable baseline
* No hyperparameter tuning required (time-constrained project)
* Fast training for iteration
* Standard approach for continuous prediction

#### 4. Training Data
**Source:** Bitcoin hourly OHLCV data (mouadja02/bitcoin-hourly-ohclv-dataset)

**Timeframe:** 2020-2025 (5 years, ~48,000 samples)
* Gap-free continuous data
* Modern market structure (post-ETF, institutional adoption)
* Includes multiple market cycles (bull, bear, recovery)

**Features (14 total):**
* Price momentum: return_1h, return_4h, return_12h, return_24h
* Trend indicators: RSI, ma_10, ma_20, ma_50, dist_from_ma10, dist_from_ma20
* Volume signals: volume_change, volume_ratio
* Volatility measures: volatility_24h, price_range

**Target:** 4-hour ahead percentage return (shift(-4))

**Data Quality:**
* 95.4% retention after cleaning
* Zero time gaps in 2020-2025 period
* Validated against historical events

#### 5. Heuristics and Assumptions
**Market Assumptions:**
* Technical indicators contain predictive information (tested via H1)
* Recent data more relevant than historical (2020+ focus)
* 4-hour timeframe balances signal vs noise

**Feature Engineering Assumptions:**
* Momentum indicators capture trend continuation
* Mean reversion captured by MA distance
* Volume changes indicate conviction
* Volatility measures risk

**Model Assumptions:**
* Linear relationships between features and returns
* Stationarity within training window
* Past patterns repeat in future

**Limitations Discovered:**
* Market exhibits near-random walk at 4-hour scale
* Linear model insufficient for complex price dynamics
* Technical indicators alone lack predictive power

## Dashboard Design

Page 1: 📊 Project Summary
* Overview & business requirements
* Dataset information
* Key findings (honest metrics)
* Important disclaimers

Page 2: 📈 Data Study
* Correlation analysis
* Feature importance charts
* Data quality notes

Page 3: 🎯 Price & Trade Predictor
* 14 interactive sliders
* BR1 regression prediction
* BR2 classification prediction
* Risk assessment

Page 4: 🔬 Hypothesis Validation
* H1: Price predictability (NOT VALIDATED)
* H2: Profitability prediction (NOT VALIDATED)
* H3: Data quality (PARTIAL)
* Scientific value explanation

Page 5: ⚙️ Technical Overview
* Model specifications
* Performance metrics
* Tech stack
* Assessment criteria met


## Knonw Issues & Unfixed Bugs
1. Negative R² Score in Regression Model
**Issue:** R² = -0.037 (negative indicates model predicts worse than baseline mean)
**Why Unfixed:** This is not a bug—it is a valid finding. The model mathematically works correctly; the market data simply does not contain sufficient predictive signal for the model to beat a naive baseline at 4-hour timeframes.
**Impact:** Regression predictions have no reliability for actual trading decisions.
**Mitigation:** Dashboard includes prominent warnings about weak predictive power. Educational framing emphasizes negative results are scientifically valid.

2. Classification Model Near-Random Performance
**Issue:** 51% accuracy (only 1% better than coin flip), ROC-AUC = 0.5375
**Why Unfixed:** Not a bug—reflects true difficulty of binary direction prediction at short timescales. The classification pipeline is technically correct; the problem itself is extremely hard.
**Impact:** Binary predictions unreliable for decision-making.
**Mitigation:** Probability outputs centered near 0.5 (50%) make uncertainty explicit. Dashboard disclaimers prevent misuse.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

