import os
import csv
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# --- Configuration ---
# Replace with your Supabase credentials (now loaded from .env)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CSV_FILE_PATH = r"C:\Users\faisa\OneDrive\Desktop\AI Engineer\agent auto\products_database_named.csv" # The specific CSV file for products
TABLE_NAME = "products"

# Ensure credentials are loaded
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials not found. Make sure .env file is correctly configured.")

# --- Supabase Client Initialization ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- CSV Processing and Upload Function ---
def process_and_upload_csv(file_path: str):
    print(f"Processing file: {file_path}")
    try:
        df = pd.read_csv(file_path)

        # Rename columns to match Supabase table schema
        # This mapping ensures the CSV columns match the database columns exactly
        column_mapping = {
            "product_id": "product_id",
            "product_name": "product_name",
            "category": "category",
            "price": "price",
            "stock_quantity": "stock_quantity",
            "last_updated": "last_updated",
        }

        # Apply mapping and drop columns not in our schema
        df = df.rename(columns=column_mapping)
        
        # Filter to only include columns that are in our Supabase 'products' table schema
        # We need to make sure 'id' is not included here as Supabase generates it.
        supabase_schema_columns = [
            "product_id", "product_name", "category", "price", "stock_quantity", "last_updated"
        ]
        df = df[df.columns.intersection(supabase_schema_columns)]
        
        # Convert all relevant columns to string type and replace 'nan' and empty strings with None
        for col in df.columns:
            if col in supabase_schema_columns: # Only apply to columns we intend to upload
                df[col] = df[col].astype(str).replace('nan', None).replace('', None)

        # Convert DataFrame to a list of dictionaries (JSON format) for Supabase insertion
        records = df.to_dict(orient="records")

        if not records:
            print(f"No records found in {file_path} after processing. Skipping.")
            return

        # Insert data into Supabase
        try:
            res = supabase.table(TABLE_NAME).insert(records).execute()
            if res.data:
                print(f"Successfully uploaded {len(res.data)} records from {file_path} to Supabase.")
            elif res.count is not None:
                print(f"Successfully uploaded {res.count} records from {file_path} to Supabase (count from Supabase).")
            else:
                print(f"Warning: Supabase insert operation for {file_path} completed but no data returned in response.")
        except Exception as supabase_error:
            print(f"Error uploading data from {file_path} to Supabase: {supabase_error}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except pd.errors.EmptyDataError:
        print(f"Warning: {file_path} is empty. Skipping.")
    except Exception as e:
        print(f"An unexpected error occurred while processing {file_path}: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    if not os.path.exists(CSV_FILE_PATH):
        print(f"Error: CSV file '{CSV_FILE_PATH}' does not exist.")
    else:
        process_and_upload_csv(CSV_FILE_PATH)
        print("CSV file processed.")
