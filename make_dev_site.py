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

# Example warning
    logging.warning('Watch out')
# Example info
    logging.info('This is the info')

    #cd_path = 'cd ' + destination
    #process = shell_command(cd_path)

    print '---non function print---'
    print subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True).stdout.read()

    print '+++function print+++'
    print shell_command('pwd')

    print '```function logging print```'
    logging.info(shell_command('pwd'))

    #print process.stdout.read()
    #logging.info(shell_command('pwd'))

    #shell_command('git status')

# Parse commands for python
def shell_command(command):
# Split the commands into a list for Popen
    print '===in shell_commnd function==='
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()

if __name__ == "__main__":
    main()
