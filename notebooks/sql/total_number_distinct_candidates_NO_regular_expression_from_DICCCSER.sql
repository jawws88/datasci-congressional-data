--results: 341 distinct candidate_name with NO regular expression

select count( sub.name) as distinct_original_names_dicccser
from (
  select
    distinct(candidate_name) as name
  from data_ingest.casos__california_candidate_statewide_election_results
  where county_name = 'State Totals' and contest_name <> 'President' and contest_name <> 'US Senate - 1'
)sub