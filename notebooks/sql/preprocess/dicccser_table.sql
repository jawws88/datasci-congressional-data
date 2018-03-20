https://modeanalytics.com/editor/code_for_san_francisco/reports/80fe013bbf32

--data_ingest.casos__california_candidate_statewide_election_results
--goal - ID number of missing values in each attribute.

select count(*),
candidate_name -- 40 empty/null
--contest_name
--county_name
--election_name
--incumbent_flag
--party_name -- 40 empty/null
--vote_total -- 40 empty/null

from data_ingest.casos__california_candidate_statewide_election_results
 where county_name like 'State Totals' 
    and contest_name not like 'President%'
    and contest_name not like 'president%'
    and contest_name not like 'US Senate%' 
    and contest_name not like 'United States Representative%'
    and contest_name not like 'us'
    and contest_name not like 'united%'
    and contest_name not like '%Congressional District'


group by
candidate_name
--contest_name 
--county_name
--election_name
--incumbent_flag
--party_name
--vote_total

order by 
candidate_name
--contest_name 
--county_name
--election_name
--incumbent_flag
--party_name
--vote_total
desc
