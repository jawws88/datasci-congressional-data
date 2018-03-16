--results: 169 distinct candidate name matches with regular expression

with table_one as
(
select
  recipient_candidate_name, 
  count(recipient_candidate_name) as occur_one,
  regexp_replace(lower(split_part(recipient_candidate_name, ',', 2) || split_part(recipient_candidate_name, ',', 1)), '[^a-z]', '', 'g') as re_name_one
from trg_analytics.candidate_contributions
group by recipient_candidate_name
),

table_two as
(
select
  candidate_name, 
  count(candidate_name) as occur_two,
  regexp_replace(lower(split_part(candidate_name, ',', 2) || split_part(candidate_name, ',', 1)), '[^a-z]', '', 'g') as re_name_two
 from data_ingest.casos__california_candidate_statewide_election_results
 where county_name = 'State Totals' and contest_name <> 'President' and contest_name <> 'US Senate - 1'
 group by candidate_name
)

select count(sub.temp )
from (

    select
      candidate_name,
      table_one.re_name_one as temp,
      table_one.occur_one,
      recipient_candidate_name,
      table_two.re_name_two,
      table_two.occur_two
    from table_two
    join table_one
    on re_name_one = re_name_two
    order by re_name_one
) sub
