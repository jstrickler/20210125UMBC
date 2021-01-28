#!/usr/bin/env python3
import sys


def main():
    sys.stdout.write("Please enter some text:\n")
    x = sys.stdin.readline()
    # Use of literal fstring instead of format method
    sys.stdout.write(f"Standard Output\n{x}")
    sys.stderr.write(f"Error Output\n{x}")
    print(f"Error Output\n{x}", file=sys.stderr)

    # F.read() F.readline() F.readlines() F.write() F.writelines() F.seek() F.tell()


if __name__ == "__main__":
    main()
