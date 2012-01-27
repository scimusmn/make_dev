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
    #logging.warning('Watch out')
# Example info
    #logging.info('This is the info')

# ---Git process---
    os.chdir(destination)

    #logging.info(call_command('git status'))

    output,_ = (call_command('git status'))
    match = re.search('# On branch ([^\s]*)', output)
    branch = None
    if match is None:
        raise Exception('Could not get status')
    #elif match.group(1) == 'master':
        #raise Exception('You must be in the branch that you want to merge, not master')
    else:
        branch = match.group(1)
        logging.info('On branch %s' % branch)

# Parse commands for python
def call_command(command):
    process = subprocess.Popen(command.split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
    )
    return process.communicate()

if __name__ == "__main__":
    main()
