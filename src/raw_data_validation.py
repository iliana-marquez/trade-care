"""
TradeCare Raw Data Validation Module

Centralized validation for raw Bitcoin hourly data fetched from GitHub.
Ensures data integrity and security before it enters the ML pipeline.

This module is specifically for raw data validation at the collection stage so it passes securely
to the next processing stages (cleaning, transformations, etc).
"""

import pandas as pd
from datetime import datetime


# Data source URL
DATA_URL = "https://github.com/mouadja02/bitcoin-hourly-ohclv-dataset/blob/main/btc-hourly-price_2015_2025.csv"