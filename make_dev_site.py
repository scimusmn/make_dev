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

    try:
        os.mkdir(destination)
    except OSError as e:
        if 'File exists' in e.strerror:
            print 'The destination already exists. Would you like to overwrite it? This will result in complete data loss of the existing files.'
            sys.exit('Exiting')

# Change directories to the destination
    try:
        os.chdir(destination)
    except OSError as e:
        print 'There was a problem navigating to your destination'
        print e.strerror + e.filename
        sys.exit('Exiting')

# Assign the stdout from the communicate() tuple to output
# Assign the stderr from the tuple to _ a throw away variable in Python
    output,_ = (call_command('git status'))

    match = re.search('# On branch ([^\s]*)', output)
    branch = None
    if match is None:
        raise Exception('Your destination is not a git repo.')
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
# Returns a tuple of the stdout and stderr
    return process.communicate()

# Query users for a yes or no response
def query_yes_no(question, default="yes"):
    valid = {"yes":True, "y":True, "ye":True,
            "no":False, "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer '%s'" % default)

    while True:
        sys.stdout.write( question + prompt )
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

if __name__ == "__main__":
    main()
