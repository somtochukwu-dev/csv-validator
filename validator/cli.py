import argparse
import pandas as pd
from validator.core import validate_schema, check_nulls, check_types, check_duplicates

def main():
    parser = argparse.ArgumentParser(description="CSV Validator CLI")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--schema", nargs="+", help="Expected columns")
    parser.add_argument("--types", nargs="+", help="Column:type pairs (e.g. age:int email:str)")
    parser.add_argument("--check-dupes", action="store_true", help="Check duplicates")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)

    if args.schema:
        print("Schema valid:", validate_schema(df, args.schema))

    if args.types:
        schema = dict(item.split(":") for item in args.types)
        print("Type checks:", check_types(df, schema))

    print("Nulls:", check_nulls(df))

    if args.check_dupes:
        print("Duplicates:", check_duplicates(df))

if __name__ == "__main__":
    main()
