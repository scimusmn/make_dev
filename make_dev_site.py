#!/usr/bin/env python
# make_dev_site.py

import os
import re
import subprocess
import logging
import argparse

def main():

    parser = argparse.ArgumentParser(description='Make a dev site.')
    parser.add_argument('giturl',
            help='URL of the git repo.')
    parser.add_argument('destination',
            help='Path to a destination for your clone')

    parser.add_argument('-b', '--branch', default='master',
            help='Git branch to clone')

# Have this set a default to the git's repo name after the repo is fetched
    #parser.add_argument('-n', '--name', default=parser.parse_args().giturl.repo_name,
            #help='Git branch to clone')

    args = parser.parse_args()

# Parse commands for python
def shell_command(command):
# Split the commands into a list for Popen
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

if __name__ == "__main__":
    main()
