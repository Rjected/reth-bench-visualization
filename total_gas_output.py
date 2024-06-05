import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_gas_usage_per_second(file_path):
    # Load data from CSV file
    # NOTE: the CSV file takes also accounts for any inter-block-processing
    # latency incurred by the benchmarker, for example if the benchmarker is
    # taking a while to fetch blocks, that will be accounted for
    df = pd.read_csv(file_path)

    # Calculate time diffs and gas per second. Note that the csv outputs
    # duration in microseconds
    df['time_diff'] = df['time'].diff().fillna(df['time'])

    # Microsecond to second conversion
    df['gas_per_second'] = (df['gas_used'] * 1_000_000 / df['time_diff'])

    # Plotting the data
    plt.figure(figsize=(12, 6))
    # Convert gas to MGas so the graph is readable
    plt.plot(df['block_number'], df['gas_per_second'] / 1_000_000, linestyle='-')
    plt.title('Gas Usage Per Second by Block Number')
    plt.xlabel('Benchmark block')
    plt.ylabel('MGas Per Second')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
    else:
        file_path = sys.argv[1]
        plot_gas_usage_per_second(file_path)
