# reth-bench visualization

This repository contains Python scripts for visualizing benchmark data from the `reth-bench` command.
Each script takes a CSV file as input and produces graphs that visualize a single benchmark run.

## Scripts

### Gas Usage Per Second

This plots the gas per second across the entire duration of a benchmark.
This accounts for any delays in fetching blocks from a data source, so may be only a rough estimate of block processing throughput.

#### Usage

```bash
python total_gas_output.py <path_to_csv_file>
```

### RPC Latency Comparison

This script analyzes the latency for two types of RPC calls: `newPayload` and `forkchoiceUpdated`. It plots the latency of each call in the input.
It also plots the gas per second, using only the duration of the engine RPC calls as the time taken to process a block.
This may be more accurate as it does not include the time taken to fetch blocks from a data source.

#### Usage

```bash
python combined_latency_output.py <path_to_csv_file>
```

## Installation

To run these scripts, you will need Python, matplotlib, and pandas installed:

```bash
# Clone the repository
git clone https://github.com/rjected/reth-bench-visualization.git
cd reth-bench-visualization

# venv, activate etc...

# Install dependencies
pip install -r requirements.txt

# Run the scripts
python total_gas_output.py <path_to_csv_file>
python combined_latency_output.py <path_to_csv_file>
```

## Data Format

### Gas Usage

The expected CSV format follows the output of the `reth-bench` command:

```
block_number,gas_used,time
19600001,13831756,341350
19600002,18131995,1326017
...
```

### RPC Latency

The expected CSV format follows the output of the `reth-bench` command:

```
gas_used,new_payload_latency,fcu_latency,total_latency
13831756,120259,212107,332367
18131995,672227,312281,984508
...
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
