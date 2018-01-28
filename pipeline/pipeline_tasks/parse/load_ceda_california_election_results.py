"""
Load CEDA California Election Results Data

Source of data: https://maplight.org/data_guide/california-money-and-politics-bulk-data-set/

Data Dictionary: http://www.csus.edu/isr/projects/ceda%20reports/codebook2016.pdf

Likely will want to use API in the future for more dynamic ETL.
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


def load_datasets(dbm, direc):
    """CEDA Election Results Data

    Keyword Args:
        dbm: DBManager object
        dir: Directory where files are
    """
    filenames = os.listdir(direc)
    files = [filename for filename in filenames if filename.endswith('xls') or filename.endswith('xlsx')]

    column_map_cand = {
        'RACEID': 'race_id',
        'RaceID': 'race_id',
        'RecordID': 'record_id',
        'CO': 'co',
        'JUR': 'jur',
        'CNTYNAME': 'cntyname',
        'YEAR': 'year',
        'DATE': 'date',
        'PLACE': 'place',
        'CSD': 'csd',
        'OFFICE': 'office',
        'RECODE_OFFICE': 'recode_office',
        'RECODE_OFFNAME': 'recode_offname',
        'AREA': 'area',
        'TERM': 'term',
        'VOTE#': 'vote_number',
        'LAST': 'last',
        'FIRST': 'first',
        'BALDESIG': 'baldesig',
        'INCUMB': 'incumb',
        'INC': 'inc',
        'NUM_INC': 'num_inc',
        'Num_Inc': 'num_inc',
        'CAND#': 'cand_number',
        'VOTES': 'votes',
        'WRITEIN': 'writein',
        'SUMVOTES': 'sumvotes',
        'VOTES_sum': 'sumvotes',
        'TOTVOTES': 'totvotes',
        'RVOTES': 'rvotes',
        'PERCENT': 'percent',
        'Percent': 'percent',
        'ELECTED': 'elected',
        'elected': 'elected',
        'RUNOFF': 'runoff',
        'runoff': 'runoff',
        'CHECKRUNOFF': 'checkrunoff',
        'checkrunoff': 'checkrunoff',
        'Multi_RaceID': 'multi_race_id',
        'Multi_CandID': 'multi_cand_id',
        'Multi_CO': 'multi_co',
        'Indivtotal_votes': 'indivtotal_votes',
        'indivtotal_votes': 'indivtotal_votes',
        'Multitotal_votes': 'multitotal_votes',
        'multitotal_votes': 'multitotal_votes',
        'Total_writein': 'total_writein_votes',
        'total_writein': 'total_writein_votes',
        'Total_writein_votes': 'total_writein_votes',
        'Totalwritein_votes': 'total_writein_votes',
        'Newtotvotes': 'newtovotes',
        'newtotvotes': 'newtovotes',
        'Rindivto': 'rindivto',
        'Newelected': 'newelected',
        'newelected': 'newelected',
    }


    # column_map_cand = {
    #     'RACEID': 'race_id',
    #     'RaceID': 'race_id',
    #     'RecordID': 'record_id',
    #     'CO': 'co',
    #     'JUR': 'jur',
    #     'CNTYNAME': 'county_name',
    #     'YEAR': 'election_year',
    #     'DATE': 'date_of_election',
    #     'PLACE': 'political_jurisdiction',
    #     'CSD': 'csd',
    #     'OFFICE': 'office',
    #     'RECODE_OFFICE': 'office_code',
    #     'RECODE_OFFNAME': 'office_code_name',
    #     'AREA': 'area_within_office',
    #     'TERM': 'term_of_office',
    #     'VOTE#': 'number_seats_to_be_filled',
    #     'LAST': 'candidate_last_name',
    #     'FIRST': 'candidate_first_name',
    #     'BALDESIG': 'candidate_ballot_designation',
    #     'INCUMB': 'incumbency_status',
    #     'INC': 'incumbency_status',
    #     'NUM_INC': 'incumbency_status_numeric',
    #     'Num_Inc': 'incumbency_status_numeric',
    #     'CAND#': 'number_candidates_running',
    #     'VOTES': 'number_votes_for_candidate',
    #     'WRITEIN': 'total_write_in_votes_for_candidates_not_listed',
    #     'SUMVOTES': 'total_votes_for_candidates_running_not_write_ins',
    #     'VOTES_sum': 'total_votes_for_candidates_running_not_write_ins',
    #     'TOTVOTES': 'total_votes_for_all_candidates',
    #     'RVOTES': 'rank_order_candidates',
    #     'PERCENT': 'percent_of_votes_received_by_candidate',
    #     'Percent': 'percent_of_votes_received_by_candidate',
    #     'ELECTED': 'candidate_election_outcome',
    #     'elected': 'candidate_election_outcome',
    #     'RUNOFF': 'potential_runoff_candidates',
    #     'runoff': 'potential_runoff_candidates',
    #     'CHECKRUNOFF': 'confirmed_runoff_candidates',
    #     'checkrunoff': 'confirmed_runoff_candidates',
    #     'Multi_RaceID': 'election_race_id_mult_county',
    #     'Multi_CandID': 'candidate_id_mult_county',
    #     'Multi_CO': 'multi_county_race_indicator',
    #     'Indivtotal_votes': 'multi_county_candidate_votes',
    #     'indivtotal_votes': 'multi_county_candidate_votes',
    #     'Multitotal_votes': 'multi_candidate_votes_all_candidates_not_write_ins',
    #     'multitotal_votes': 'multi_candidate_votes_all_candidates_not_write_ins',
    #     'Total_writein': 'multi_county_total_write_in_votes',
    #     'total_writein': 'multi_county_total_write_in_votes',
    #     'Total_writein_votes': 'multi_county_total_write_in_votes',
    #     'Totalwritein_votes': 'multi_county_total_write_in_votes',
    #     'Newtotvotes': 'multi_county_votes_all_candidates',
    #     'newtotvotes': 'multi_county_votes_all_candidates',
    #     'Rindivto': 'multi_county_rank_order_candidates',
    #     'Newelected': 'multi_county_candidate_election_outcome',
    #     'newelected': 'multi_county_candidate_election_outcome',
    # }

    # dtype_map = {
    #     'recipient_candidate_district': sa.types.String,
    #     'recipient_candidate_office': sa.types.String,
    # }

    # Reading and Writing Candidate Files
    dfs = []
    for f in files:
        print('Reading file {} into pandas.'.format(f))
        year = re.findall(r'\d+', f)[0]
        if year == '2014' or year == '2015':
            sheet_name = 'candidates{}'.format(year)
        elif year == '2016':
            sheet_name = 'Candidates_{}'.format(year)
        else:
            sheet_name = 'Candidates{}'.format(year)
        print(sheet_name)
        df = pd.read_excel(os.path.join(direc, f), sheet_name=sheet_name)
        
        # Doing some relatively hacky file specific fixes since not 100% standard format
        if year == '2011' or year == '2013' or year == '2014' or year == '2015':
            df.drop(columns=['RACEID'], inplace=True)

        df.rename(index=str, columns=column_map_cand, inplace=True)
        print(year)
        print(df.columns)
        dfs.append(df)

    print('Writing candidate election results into database.')
    df = pd.concat(dfs, ignore_index=True)
    dbm.write_df_table(
        df,
        table_name='ceda__california_candidate_election_results',
        schema='data_ingest')

    # # Reading and Writing Other Files
    # dfs = []
    # for f in other_files:
    #     print('Reading file {} into pandas.'.format(f))
    #     df = pd.read_csv(os.path.join(direc, f))
    #     df.rename(index=str, columns=column_map, inplace=True)
    #     dfs.append(df)

    # print('Writing other files into database.')
    # df = pd.concat(dfs, ignore_index=True)
    # dbm.write_df_table(
    #     df,
    #     table_name='maplight__california_other',
    #     schema='data_ingest')


def main():
    """Execute Stuff"""
    print('Parsing and Loading California Election Results Data')
    args = get_args()
    dbm = DBManager(db_url=args.db_url)
    git_root_dir = uf.get_git_root(os.path.dirname(__file__))
    directory = os.path.join(git_root_dir, 'src', 'ceda')
    load_datasets(dbm, directory)


if __name__ == '__main__':
    """See https://stackoverflow.com/questions/419163/what-does-if-name-main-do"""
    main()

