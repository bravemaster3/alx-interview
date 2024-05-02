#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics:"""

import sys
import re

fp = (
    r'\s*(?P<ip>\S+)\s*',
    r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
    r'\s*"(?P<request>[^"]*)"\s*',
    r'\s*(?P<status_code>\S+)',
    r'\s*(?P<file_size>\d+)'
)
pattern = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])

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
        if re.fullmatch(pattern, line):
            line_split = line.split(" ")
            if int(line_split[-2]) in status_counts:
                status_counts[int(line_split[-2])] += 1
            file_size += int(line_split[-1])

        counter += 1
        if (counter % 10 == 0):
            print_statistics()

    # Check for EOF (end of file)
    if counter % 10 != 0:  # If the last batch of lines is less than 10
        print_statistics()

except (KeyboardInterrupt, EOFError):
    print_statistics()
