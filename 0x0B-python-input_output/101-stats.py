#!/usr/bin/python3
"""Read stdin"""
import sys
import signal

data = {"File size": 0}


def print_stats(data):
    """Print stats about the data read from stdin."""
    for key in data:
        print("%s: %d" % (key, data[key]))


def signal_handler(signal_num, frame):
    """Handle signals"""
    print_stats(data)
    # raise KeyboardInterrupt


if __name__ == "__main__":
    count = 0
    signal.signal(signal.SIGINT, signal_handler)
# try:
    for line in sys.stdin:
        count += 1
        line = line.strip()
        line_data = line.split(" ")
        data["File size"] += int(line_data[-1])
        data[line_data[-2]] = data[line_data[-2]] + \
            1 if line_data[-2] in data else 1
        if count % 10 == 0:
            print_stats(data)
# except KeyboardInterrupt:
    print_stats(data)
