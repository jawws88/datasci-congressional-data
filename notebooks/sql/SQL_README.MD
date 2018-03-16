### Merge Election Results and Candidate Contributions Data Together Documentation

> This is the link to Mode Analytics workspace.

[https://modeanalytics.com/editor/code_for_san_francisco/reports/d4e007734c45](https://modeanalytics.com/editor/code_for_san_francisco/reports/d4e007734c45)

* Q1 - results: 169 distinct candidate name MATCHES with regular expression
* Q3 - results: 1550 recipient_candidate_name with regular expression
* Q5 - results: 336 candidate_names with regular expression

* Q21 - results: 341 distinct candidate_name with NO regular expression
* Q22 - results: 1563 distinct recipient_candidate_name with NO regular expression

> 169/336 = 0.50297619 

### Additional Notes:

* trg_analytics.candidate_contributions => TACC
 
* data_ingest.casos__california_candidate_statewide_election_results => DICCCSER

* Election cycle is for the upcoming election. eg - 2015 election cycle is for the 2016 election in the TACC table.

* Candidate name with an asterisk in DICCCSER is the incumbent as indicated in [http://elections.cdn.sos.ca.gov/sov/2014-general/pdf/06-summary.pdf](http://elections.cdn.sos.ca.gov/sov/2014-general/pdf/06-summary.pdf)


