import os
import pandas as pd

def convert_csv_to_xlsx(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]

    for csv_file in csv_files:
        # Create the full file paths for the input and output files
        csv_file_path = os.path.join(input_folder, csv_file)
        xlsx_file_name = os.path.splitext(csv_file)[0] + ".xlsx"
        xlsx_file_path = os.path.join(output_folder, xlsx_file_name)

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file_path)

        # Save the DataFrame to an Excel file
        df.to_excel(xlsx_file_path, index=False)
        print(f"Data exported to {xlsx_file_path}")