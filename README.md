# Illumio-Technical-Assessment

# Flow Log Parser

## Assumptions
- Supports only default log format (version 2).
- Tag lookup table is a CSV file (`dstport, protocol, tag`).
- Case-insensitive matching for protocol and tags.
- Handles flow logs up to 10 MB and lookup tables with up to 10,000 mappings.
- No external libraries required, works with Python 2.x.

## How to Run
1. Clone/download the repo.
2. Ensure Python 2.x is installed.
3. Place `flow_log.txt` and `lookup_table.csv` in the same folder as the script.
4. Run the script:
    ```bash
    python flow_log_parser.py
    ```
5. Output (`output.csv`) will be generated in the same directory.

## Files
- `flow_log_parser.py`: Main program.
- `flow_log.txt`: Sample flow log file.
- `lookup_table.csv`: Sample lookup table.
- `output.csv`: Generated output with tag and port/protocol counts.

## Tests
- Tested with small (14 entries) and large datasets (~10 MB logs).
- Verified case-insensitive matching and handling of edge cases.
