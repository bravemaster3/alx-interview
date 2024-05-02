#!/usr/bin/env python3
import re

lines = [
    '65.254.157.184 - "GET /projects/260 HTTP/1.1" 401 974',
    '152.202.21.169 - [2024-05-02 19:05:16.134624] "GET /projects/260 HTTP/1.1" 200 457',
    '77.58.91.146 - [2024-05-02 19:05:16.442801] "GET /projects/260 HTTP/1.1" 404 139',
    '11.63.216.251 - [2024-05-02 19:05:16.701836] "GET /projects/260 HTTP/1.1" 500 83',
    '183.152.201.126 - [2024-05-02 19:05:17.353510] "GET /projects/260 HTTP/1.1" 400 654',
    '99.87.39.223 - [2024-05-02 19:05:18.144504] "GET /projects/260 HTTP/1.1" 200 621'
]

pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/\d+ HTTP/1\.1" \d+ \d+$'

for line in lines:
    if re.match(pattern, line):
        print(f"The line '{line}' matches the format.")
    else:
        print(f"The line '{line}' does not match the format.")
