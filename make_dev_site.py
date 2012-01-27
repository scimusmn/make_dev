#!/usr/bin/env python
# make_dev_site.py

import os
import sys
import re
import subprocess
import logging
import argparse
import glob

logging.basicConfig(level=logging.INFO,
        format='%(levelname)s %(message)s')

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
    destination = args.destination

# ---EXAMPLES---
# Example warning
    logging.warning('Watch out')
# Example info
    logging.info('This is the info')

# ---Git process---
    logging.info(call_command('pwd'))

    os.chdir(destination)

    logging.info(call_command('git status'))

# Parse commands for python
def call_command(command):
    process = subprocess.Popen(command.split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
    return process.communicate()

if __name__ == "__main__":
    main()
