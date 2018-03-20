with candidate_donations as
(
select
  regexp_replace(lower(split_part(recipient_candidate_name, ',', 2) || split_part(recipient_candidate_name, ', ', 1)), ' |\.|,|"|-|''|\(|\)', '', 'g') as full_name,
  sum(transaction_amount) as total_transaction
from trg_analytics.candidate_contributions
where election_cycle = '2015'
group by recipient_candidate_name
),

election_results as
(
select
  contest_name,
  regexp_replace(lower(candidate_name), ' |\.|,|"|-|''|\(|\)', '', 'g')  as candidate_name,
  vote_total,
  rank() over (partition by contest_name order by vote_total desc) = 1 as is_winner
from data_ingest.casos__california_candidate_statewide_election_results
 where county_name = 'State Totals' and contest_name <> 'President' and contest_name <> 'US Senate - 1'
   and contest_name not like 'United States Representative%'
)

select
  candidate_name,
  total_transaction,
  is_winner::int as is_winner
from candidate_donations
join election_results
on candidate_donations.full_name = election_results.candidate_name

