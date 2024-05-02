#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics:"""

import sys
import re


pattern = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
    r'"GET /projects/\d+ HTTP/1\.1" \d+ \d+$'
)

status_counts = {200: 0,
                 301: 0,
                 400: 0,
                 401: 0,
                 403: 0,
                 404: 0,
                 405: 0,
                 500: 0}
file_size = 0
counter = 0


def print_statistics() -> None:
    """routine for printing statistics"""
    print(f"File size: {file_size}")
    for k, v in status_counts.items():
        if (v > 0):
            print(f"{k}: {v}")


try:
    for line in sys.stdin:
        # print(line)
        if re.match(pattern, line):
            line_split = line.split(" ")
            if int(line_split[-2]) in status_counts:
                status_counts[int(line_split[-2])] += 1
            file_size += int(line_split[-1])

        counter += 1
        if (counter % 10 == 0):
            print_statistics()

except (KeyboardInterrupt, EOFError):
    print_statistics()
