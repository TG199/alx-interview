#!/usr/bin/python3
"""
Log Parser Script
"""
import sys
import re
from collections import defaultdict


def parse_log_line(line):
    """
    Parse a single log line and extract the status code and file size.

    Args:
        line (str): A single line from the log file.

    Returns:
        tuple: (status_code, file_size) if the line matches the expected format,
               otherwise (None, None).
    """
    pattern = r'^[\d\.]+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing the count of each status cod.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status.isdigit():
            print(f"{status}: {status_counts[status]}")

def main():
    """
    Main function to process log lines and compute statistics.
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[str(status_code)] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
