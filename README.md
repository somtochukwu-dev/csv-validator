# CSV Validator CLI

A command-line tool to validate CSV files for schema, nulls, types, and anomalies.

## Usage

```bash
python -m validator.cli sample_data/good.csv --schema id name age --types id:int name:str age:int --check-dupes
