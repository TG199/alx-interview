#!/usr/bin/python3
"""log parsing module"""

import sys


def log_data(ts, scode):
    """
    Print statistics based on the total file
    size and the counts of each
    status code.

    Args:
        ts (int): The total size of all files processed.
        scode (dict): A dictionary containing counts of
        each status code

    Returns:
        None
    """
    print(f"File size: {ts}")
    for code, count in sorted(scode.items()):
        print(f"{code}: {count}")


def parse_line(data):
    """
    Parse a log line to extract relevant information.

    Args:
        line (str): A single log line to be parsed.

    Returns:
        tuple or None: A tuple containing the IP address,
        status code, and file size if parsing is successful,
        otherwise None.
    """
    parts = data.split()
    if len(parts) < 9:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None
    return ip_address, int(status_code), int(file_size)


def main():
    """
    Main function to read log lines from stdin, parse
    them, compute statistics, and print them.

    Returns:
        None
    """
    ts = 0
    scode = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed = parse_line(line)
            if parsed is None:
                continue
            ip_address, status_code, file_size = parsed
            ts += file_size
            scode[status_code] = scode.get(
                status_code,
                0
                ) + 1

            if i % 10 == 0:
                log_data(ts, scode)
    except KeyboardInterrupt as e:
        pass

    log_data(ts, scode)


if __name__ == "__main__":
    main()