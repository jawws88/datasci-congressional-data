"""
Clean CA SOS Statewide ELection Results

Source of data: http://www.sos.ca.gov/elections/prior-elections/statewide-election-results/

For years prior 2016, the California Secretary of State provide non-relational DB formats for
election results. Clean each years' files and for each year aggregate into one CSV file.

The output for each year should be a file called "csv-candidates-YYYY.xls" into the
https://github.com/sfbrigade/datasci-congressional-data/tree/master/src/casos folder.

We can then use load_casos_california_statewide_election_results.py to load those files in.
"""
import argparse
import glob
import os
import re

import pandas as pd
import sqlalchemy as sa

from utilities.db_manager import DBManager
from utilities import util_functions as uf


def get_args():
    """Use argparse to parse command line arguments."""
    parser = argparse.ArgumentParser(description='Runner for tasks')
    parser.add_argument('--db_url', help='Database url string to the db.', required=True)
    return parser.parse_args()


def clean_datasets(dbm, direc):
    """
    CA SOS Statewide Election Data

    Keyword Args:
        dbm: DBManager object
        dir: Directory where files are
    """
    pass


def main():
    """Execute Stuff"""
    print('Cleaning California Statewide Election Results Data')
    args = get_args()
    dbm = DBManager(db_url=args.db_url)
    git_root_dir = uf.get_git_root(os.path.dirname(__file__))
    directory = os.path.join(git_root_dir, 'src', 'casos')
    clean_datasets(dbm, directory)


if __name__ == '__main__':
    """See https://stackoverflow.com/questions/419163/what-does-if-name-main-do"""
    main()

