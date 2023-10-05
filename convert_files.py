# convert_files.py
import numpy as np
import pyedflib
import pandas as pd
import os
from edf_export import edf_to_csv


def convert_multiple_files(input_directory, output_directory):
    # Get a list of all EDF files in the input directory
    edf_files = [f for f in os.listdir(input_directory) if f.endswith(".edf")]

    for edf_file in edf_files:
        # Create the full file paths for the input and output files
        edf_file_path = os.path.join(input_directory, edf_file)
        csv_file_path = os.path.join(output_directory, edf_file.replace(".edf", ".csv"))

        # Call the edf_to_csv function to convert the current EDF file to CSV
        edf_to_csv(edf_file_path, csv_file_path)
