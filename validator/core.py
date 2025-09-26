import pandas as pd

def validate_schema(df, expected_cols):
    return list(df.columns) == expected_cols

def check_nulls(df):
    return df.isnull().sum().to_dict()

def check_types(df, schema):
    results = {}
    for col, dtype in schema.items():
        if col not in df:
            results[col] = "MISSING"
            continue
        try:
            df[col].astype(dtype)
            results[col] = "PASS"
        except Exception:
            results[col] = "FAIL"
    return results

def check_duplicates(df, subset=None):
    return df.duplicated(subset=subset).sum()
