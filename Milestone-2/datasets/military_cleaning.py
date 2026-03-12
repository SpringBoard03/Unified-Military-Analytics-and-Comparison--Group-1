import pandas as pd
import re


# ---------------------------
# Standardize Column Names
# ---------------------------
def standardize_column_name(col_name):
    col_name = col_name.strip()
    col_name = col_name.lower()
    col_name = re.sub(r"[^\w\s]", "", col_name)
    col_name = re.sub(r"\s+", "_", col_name)
    return col_name


# ---------------------------
# Clean Numeric Values
# ---------------------------
def clean_numeric_value(raw_text):
    if pd.isna(raw_text):
        return raw_text

    text = str(raw_text)

    # Remove newline and tabs
    text = text.replace("\n", "").replace("\t", "")

    # Remove dollar and commas
    text = text.replace("$", "").replace(",", "")

    # Extract first numeric pattern (keeps decimals)
    match = re.search(r"\d+\.?\d*", text)
    if match:
        return match.group()
    else:
        return None


# ---------------------------
# Main Cleaning Function
# ---------------------------
def clean_dataset(input_file, output_file):

    # Read raw file
    df = pd.read_csv(input_file)

    # Standardize column names
    df.columns = [standardize_column_name(col) for col in df.columns]

    # Clean numeric columns
    for col in df.columns:
        if col != "country":  # Skip categorical column

            df[col] = df[col].apply(clean_numeric_value)
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Save without scientific notation
    df.to_csv(output_file, index=False, float_format="%.10f")

    print("Cleaning complete.")
    print("Saved as:", output_file)


# ---------------------------
# Run Script
# ---------------------------
if __name__ == "__main__":
    clean_dataset("military_raw_data.csv", "military_clean.csv")
