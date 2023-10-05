import numpy as np
import pyedflib
import pandas as pd

def edf_to_csv(edf_file_path, csv_file_path):
    # Open the EDF file
    try:
        f = pyedflib.EdfReader(edf_file_path)
    except Exception as e:
        print(f"Error opening EDF file: {e}")
        return

    # Get the signal labels and number of signals
    signal_labels = f.getSignalLabels()
    num_signals = len(signal_labels)

    # Read the signals and create a DataFrame
    df_data = {}
    for i in range(num_signals):
        signal_data = f.readSignal(i)
        df_data[f"Signal {i + 1} (µV)"] = np.round(signal_data,decimals=6)

    # Close the EDF file
    f.close()

    # Create a time array
    sample_rate = f.getSampleFrequency(0)
    num_samples = len(df_data[list(df_data.keys())[0]])
    time = np.linspace(0, num_samples / sample_rate, num_samples)

    # Add the time data to the DataFrame
    df_data['Time (Seconds)'] = np.round(time,decimals=6)

    # Create the DataFrame
    df = pd.DataFrame(df_data)

    # Reorder columns so that 'Time' comes first, then the signals
    df_columns = ['Time (Seconds)'] + [f"Signal {i + 1} (µV)" for i in range(num_signals)]
    df = df[df_columns]

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    print(f"Data exported to {csv_file_path}")
