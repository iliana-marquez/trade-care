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
- Risk scoring system categorizing trades as Low/Medium/High risk
- Explanation of factors influencing each prediction

**Benefit:** Helps traders set realistic take-profit and stop-loss levels based on expected price movement

## Hypothesis and Validation

### **1: Price Predictability from Technical Indicators**
Current market technical indicators (RSI, moving averages, volatility, volume) contain sufficient signal to predict 4-hour Bitcoin price movements with better-than-random accuracy.

**Validation:**
- Train regression model on historical data (2014-2025)
- Compare model RMSE and MAE against naive baseline (last price carried forward)
- Success criteria: RMSE < 2%, MAE < 1.5%
- Visualize prediction vs actual with scatter plot and residual analysis

### **2: Profitability Classification from Market Conditions**
Technical feature combinations (RSI levels, trend alignment, volatility, volume) can effectively classify whether a trade would be profitable.

**Validation:**
- Train classification model on historical trades (simulated from price data)
- Measure ROC-AUC score (target > 0.60 to show predictive value above random)
- Analyze feature importance to identify key contributors
- Evaluate confusion matrix and precision/recall balance




## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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

