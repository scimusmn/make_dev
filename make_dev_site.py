#!/usr/bin/env python
# make_dev_site.py

import os
import sys
import re
import subprocess
import logging
import argparse
import glob
import shutil

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

    args = parser.parse_args()
    giturl = args.giturl
    destination = args.destination
    branch = args.branch

    # Quit if the remote git repo doesn't exist.
    output,error = (call_command("git ls-remote " + giturl))
    match = re.search('ERROR', error)
    if match is not None:
        sys.exit('There was a problem with your remote repo. \n%s' % error)

    # Make the desitnation directory if it doesn't exist.
    # Quit if there is a conflict.
    try:
        os.mkdir(destination)
    except OSError as e:
        if 'File exists' in e.strerror:
            question = '''
This destination already exists.
Would you like to overwrite it?
This will completely destroy the existing files.'''
            if query_yes_no(question, default="no") == True:
                shutil.rmtree(destination)
                os.mkdir(destination)
            else:
                sys.exit("\nQuitting since you don't want to overwite the destination you provided.")

    # Change directories to the destination
    try:
        os.chdir(destination)
    except OSError as e:
        print 'There was a problem navigating to your destination'
        print e.strerror + e.filename
        sys.exit('Exiting')

    output,_ = (call_command('git init'))
    output,_ = (call_command('git remote add origin ' + giturl))
    output,_ = (call_command('git fetch'))
    output,_ = (call_command('git pull origin master'))

    if branch is not None:

        # Create a list of available remote branches

        output,_ = (call_command('git branch -a'))
        branches = output.split('\n')
        branches_available = []
        for b in branches:
            b = b.lstrip()
            match = re.search('remotes/origin/', b)
            if match is not None:
                b = b.replace('remotes/origin/','')
                branches_available.append(b)

        if branch is not in branches_available:
            sys.exit("The branch you are trying to pull doesn't exist in your remote repo.")

        sys.exit("Branch checkin completed without error.")
        output,_ = (call_command('git checkout -b ' + branch))
        output,_ = (call_command('git pull origin ' + branch))

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
