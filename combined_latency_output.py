import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_data(file_path):
    # Load data from CSV file
    df = pd.read_csv(file_path)

    # Calculate gas per second using the total latency (convert microseconds to seconds)
    df['gas_per_second'] = df['gas_used'] / df['total_latency'] * 1_000_000

    # Plotting the gas per second
    plt.figure(figsize=(12, 6))
    # Convert to MGas
    plt.plot(df.index + 1, df['gas_per_second'] / 1_000_000, linestyle='-', color='blue')
    plt.title('Gas Usage Per Second by Combined Latency')
    plt.xlabel('Benchmark block')
    plt.ylabel('MGas Per Second')
    plt.grid(True)
    plt.show()

    # Plotting latencies for RPC methods
    plt.figure(figsize=(12, 6))

    # convert to ms
    plt.plot(df.index + 1, df['new_payload_latency'] / 1_000, label='New Payload Latency', color='blue')

    # convert to ms
    plt.plot(df.index + 1, df['fcu_latency'] / 1_000, label='Forkchoice Updated Latency', color='green')
    plt.title('Latency of RPC Methods')
    plt.xlabel('Benchmark block')
    plt.ylabel('Latency (ms)')
    plt.legend()
    plt.grid(True)

    # Adjust y-axis to show labels in microseconds without scientific notation
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.0f}".format(x)))

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
    else:
        file_path = sys.argv[1]
        plot_data(file_path)
