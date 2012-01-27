#!/usr/bin/env python
# make_dev_site.py

import os
import sys
import re
import subprocess
import logging
import argparse

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

    logging.info(shell_command('git status -b'))
    logging.info(shell_command('cd ../'))
    logging.info(shell_command('ls -la'))

# Parse commands for python
def shell_command(command):
    process = subprocess.Popen(command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    ).stdout.read()

    return process

if __name__ == "__main__":
    main()
