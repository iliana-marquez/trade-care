"""
TradeCare Raw Data Validation Module

Centralized validation for raw Bitcoin hourly data fetched from GitHub.
Ensures data integrity and security before it enters the ML pipeline.

Single entry point specifically for raw data validation at the collection stage
so it passes securely to the next processing stages
(cleaning, transformations, etc).
"""

import pandas as pd
from datetime import datetime


# Data source URL
DATA_URL = "https://raw.githubusercontent.com/mouadja02/bitcoin-hourly-ohclv-dataset/main/btc-hourly-price_2015_2025.csv"

# Expected data structure
EXPECTED_COLUMNS = [
    'TIME_UNIX', 'DATE_STR', 'HOUR_STR',
    'OPEN_PRICE', 'HIGH_PRICE', 'CLOSE_PRICE', 'LOW_PRICE',
    'VOLUME_FROM', 'VOLUME_TO'
]

# Validation thresholds
MIN_EXPECTED_ROWS = 96000  # from ~ Nov 2014
MIN_TIMESTAMP = 1416031200  # Unix timestamp for 2014-11-15
MAX_PRICE = 500000  # BTC unlikely > $500k
MIN_PRICE = 0  # Prices must be positive


def fetch_and_validate_data():
    """
    Fetch and validate Bitcoin hourly data in one call.

    This is the main entry point - it handles everything:
    - Fetches data from GitHub
    - Validates structure, ranges, and integrity
    - Returns validated data or raises descriptive error

    Returns:
        pd.DataFrame: Validated Bitcoin hourly OHLCV data

    Raises:
        Exception: If data cannot be fetched
        ValueError: If data fails any validation check

    Example:
        from src.raw_data_validation import fetch_and_validate_data
        df = fetch_and_validate_data()
        # df is now guaranteed to be validated and safe to use
    """

    print("-" * 60)
    print("TradeCare Data Validation")
    print("-" * 60)

    # Step 1: Fetch
    df = _fetch_data()

    # Step 2: Validate (raises error if validation fails)
    _validate_structure(df)
    _validate_string_data(df)
    _validate_price_ranges(df)
    _validate_data_completeness(df)
    _validate_timestamps(df)

    # Step 3: Success
    print("-" * 60)
    print("All validation checks passed!")
    print(f"Data ready: {len(df):,} rows from {df['DATE_STR'].iloc[0]} to {
        df['DATE_STR'].iloc[-1]}"
        )
    print("-" * 60)

    return df


def _fetch_data():
    """
    Internal function: Fetch data from GitHub.

    Returns:
        pd.DataFrame: Raw data from URL

    Raises:
        Exception: If fetch fails
    """
    print("Fetching data from GitHub...")
    print(f"URL: {DATA_URL}")

    try:
        df = pd.read_csv(DATA_URL)
        print(f"✓ Data fetched: {len(df):,} rows & {df.shape[1]} columns")
        return df
    except Exception as e:
        raise Exception(f"Failed to fetch data: {e}")


def _validate_structure(df):
    """
    Internal function: Validate column structure.

    Ensures data has expected columns in expected order.
    Protects against repository compromise or altered structure.
    Also validates column names contain only safe characters.

    Args:
        df (pd.DataFrame): Data to validate

    Raises:
        ValueError: If structure is invalid
    """
    print("\nValidating data structure...")

    actual_columns = list(df.columns)

    # Check column structure matches expected
    if actual_columns != EXPECTED_COLUMNS:
        raise ValueError(
            f"Data structure compromised!\n"
            f"Expected columns: {EXPECTED_COLUMNS}\n"
            f"Actual columns: {actual_columns}\n"
            f"Missing: {set(EXPECTED_COLUMNS) - set(actual_columns)}\n"
            f"Extra: {set(actual_columns) - set(EXPECTED_COLUMNS)}"
        )

    # Validate column names contain only safe characters
    # Only allow: uppercase letters, underscore
    import re
    safe_pattern = re.compile(r'^[A-Z_]+$')

    for col in actual_columns:
        if not safe_pattern.match(col):
            raise ValueError(
                f"Invalid column name detected: '{col}'\n"
                f"Column names must contain only uppercaseletters and underscores.\n"
                f"Potential injection attack or data corruption."
            )

    print(f"✓ Column structure valid: {len(EXPECTED_COLUMNS)} columns present")
    print("✓ Column names safe: only alphanumeric and underscores")


def _validate_string_data(df):
    """
    Internal function: Validate string data values.

    Ensures string columns (DATE_STR, HOUR_STR) contain only safe characters.
    Protects against code injection, SQL injection, XSS attempts.

    Args:
        df (pd.DataFrame): Data to validate

    Raises:
        ValueError: If suspicious characters detected
    """
    print("Validating string data safety...")

    import re

    # Validate DATE_STR format: YYYY-MM-DD
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    invalid_dates = df[~df['DATE_STR'].astype(str).str.match(date_pattern)]

    if len(invalid_dates) > 0:
        sample = invalid_dates['DATE_STR'].iloc[0]
        raise ValueError(
            f"Invalid DATE_STR format detected: '{sample}'\n"
            f"Expected format: YYYY-MM-DD (e.g., 2024-11-21)\n"
            f"Found {len(invalid_dates)} invalid entries.\n"
            f"Potential injection attack or data corruption."
        )

    # Validate HOUR_STR: should be 0-23
    try:
        hour_values = pd.to_numeric(df['HOUR_STR'], errors='coerce')
        if hour_values.isna().any():
            raise ValueError("Non-numeric values in HOUR_STR")
        if (hour_values < 0).any() or (hour_values > 23).any():
            raise ValueError("Hour values outside 0-23 range")
    except Exception as e:
        raise ValueError(
            f"Invalid HOUR_STR values detected: {e}\n"
            f"Expected: integers 0-23\n"
            f"Potential injection attack or data corruption."
        )

    # Check for dangerous characters in string columns
    dangerous_chars = [
        '<', '>', ';', '&', '|', '$', '`', '\\', '"', "'", '(', ')'
        ]
    string_cols = ['DATE_STR', 'HOUR_STR']

    for col in string_cols:
        col_str = df[col].astype(str)
        for char in dangerous_chars:
            if col_str.str.contains(re.escape(char), regex=True).any():
                raise ValueError(
                    f"Dangerous character '{char}' detected in {col}\n"
                    f"This could indicate injection attack or data corruption.\n"
                    f"Only safe alphanumeric characters and hyphens allowed."
                )

    print("✓ String data validated: safe formats, no injection patterns")


def _validate_price_ranges(df):
    """
    Internal function: Validate price value ranges.

    Ensures prices are positive and within reasonable bounds.
    Protects against data corruption and malicious injection.

    Args:
        df (pd.DataFrame): Data to validate

    Raises:
        ValueError: If prices are invalid
    """
    print("Validating price ranges...")

    price_columns = ['OPEN_PRICE', 'HIGH_PRICE', 'LOW_PRICE', 'CLOSE_PRICE']

    for col in price_columns:
        min_val = df[col].min()
        max_val = df[col].max()

        # Check for negative prices
        if min_val < MIN_PRICE:
            raise ValueError(
                f"Invalid data: {col} contains negative values (min: {
                    min_val})"
            )

        # Check for suspiciously high prices
        if max_val > MAX_PRICE:
            raise ValueError(
                f"Suspicious data: {col} contains values > ${
                    MAX_PRICE:,} (max: ${max_val:,.2f})"
            )

    print(f"✓ Price ranges valid: all prices between $0 and ${MAX_PRICE:,}")


def _validate_data_completeness(df):
    """
    Internal function: Validate data completeness.

    Ensures dataset has minimum expected rows.
    Protects against truncated or incomplete datasets.

    Args:
        df (pd.DataFrame): Data to validate

    Raises:
        ValueError: If dataset is incomplete
    """
    print("Validating data completeness...")

    row_count = len(df)

    if row_count < MIN_EXPECTED_ROWS:
        raise ValueError(
            f"Dataset truncated: only {row_count:,} rows.\n"
            f"Expected at least {
                MIN_EXPECTED_ROWS:,} rows (Nov 2014 - present)"
        )

    print(f"✓ Row count valid: {row_count:,} rows (>= {MIN_EXPECTED_ROWS:,})")


def _validate_timestamps(df):
    """
    Internal function: Validate timestamp ranges.

    Ensures timestamps start from expected date (Nov 2014).
    Protects against wrong dataset or corrupted timestamps.

    Args:
        df (pd.DataFrame): Data to validate

    Raises:
        ValueError: If timestamps are invalid
    """
    print("Validating timestamps...")

    min_timestamp = df['TIME_UNIX'].min()

    if min_timestamp < MIN_TIMESTAMP:
        raise ValueError(
            f"Invalid timestamps: earliest is {min_timestamp}\n"
            f"Expected >= {MIN_TIMESTAMP} (Nov 2014)"
        )

    print(f"✓ Timestamps valid: starts from {df['DATE_STR'].iloc[0]}")


def get_data_info(df):
    """
    Get summary information about the dataset.

    Optional utility function for data exploration.

    Args:
        df (pd.DataFrame): Bitcoin hourly data

    Returns:
        dict: Summary statistics and metadata

    Example:
        >>> df = fetch_and_validate_data()
        >>> info = get_data_info(df)
        >>> print(info['date_range'])
    """

    return {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'columns': list(df.columns),
        'date_range': {
            'first': df['DATE_STR'].iloc[0],
            'last': df['DATE_STR'].iloc[-1]
        },
        'price_range': {
            'min': float(df['CLOSE_PRICE'].min()),
            'max': float(df['CLOSE_PRICE'].max()),
            'mean': float(df['CLOSE_PRICE'].mean())
        },
        'memory_usage_mb': float(df.memory_usage(deep=True).sum() / 1024**2),
        'fetched_at': datetime.now().isoformat()
    }
