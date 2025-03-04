#!/usr/bin/env python3

import subprocess
import os
import argparse

# This function will get the git version of the repository where the script is located.
def get_git_version():
    try:
        version = subprocess.check_output(["git", "describe", "--tags"], cwd = os.path.dirname(os.path.abspath(__file__))).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        version = "unknown"
    return version

VERSION = get_git_version()
NAME = os.path.splitext(os.path.basename(__file__))[0]

def main():
    # argparse is a module for parsing command-line arguments.
    # It allows you to define what arguments your program requires, and handles parsing those arguments from sys.argv.
    parser = argparse.ArgumentParser(description=f"{NAME} - Version {VERSION}\nA script template with argument parsing.")
    parser.add_argument('-d', '--directory', type=str, help='Directory to process', default=os.getcwd())
    parser.add_argument('-v', '--version', action='version', version=f'{NAME} - Version {VERSION}')
    args = parser.parse_args()
    current_directory = args.directory
    print(f"Processing directory: {current_directory}")

if __name__ == "__main__":
    main()
