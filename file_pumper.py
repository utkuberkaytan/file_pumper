import os
import random
import argparse

def increase_exe_size(file_path, size_increase_mb):
    size_increase_bytes = size_increase_mb * 1024 * 1024
    with open(file_path, 'ab') as f:
        f.write(os.urandom(size_increase_bytes))
    print(f"Increase completed: {file_path} size increased by {size_increase_mb} MB")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Increase the size of an executable file')
    parser.add_argument('-p', type=str, required=True, help='Path to the executable file')
    parser.add_argument('-s', type=int, required=True, help='Size increase in megabytes')

    args = parser.parse_args()
    file_path = args.path
    size_increase_mb = args.size

    print(f"Increasing size of {file_path} by {size_increase_mb} MB...")
    increase_exe_size(file_path, size_increase_mb)
    print("Operation completed successfully!")
