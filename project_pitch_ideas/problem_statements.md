# Problem Statements
In this document we list several overall "problem statements" we are focusing on.

## Problem Statement 1: Making Campaign Finance Data more transparent
A critical issue with campaign finance data is how opaque the system is. However, this data is extremely important. Funders impact who are elected officials are and may even affect how our elected officials' voting behavior. In addition, as much work that's been done on a national level, much less has been done at a local level (e.g. SF Bay Area + Monterey Bay) *How might we aggregate this data and present it in a more accessible manner?*

### Challenges

1. Extract Campaign Finance Data from [Cal-Access](http://cal-access.sos.ca.gov/Campaign/) and/or [SF Open Data](https://data.sfgov.org/City-Management-and-Ethics/Campaign-Finance-Database/sv2b-bdbj) and parse into a usable format (e.g. relational database). This will be very related, if not identical, to the work necessary to complete Problem Statement 2.
2. Visualize data on a public website/dashboard.
    1. For each election cycle/candidate can we show how much each candidate has received from which sources?
    2. Can we show how much was received at a geographic level
    3. There is actually some really great prior art here (specific to SF for the 2016 election cycle) here: https://github.com/sfbrigade/campaign_finance

## Problem Statement 2: Predicting Voting Behavior Based on Funding Sources
The reason why more transparency in campaign finance data is critical is because, unfortunately, not every official is acting in the best interest of the American public. Money talks. Lawrence Lessig (professor at Harvard Law School) gave an inspiring [TED Talk](https://www.ted.com/talks/lawrence_lessig_we_the_people_and_the_republic_we_must_reclaim) in which he describes how only the top 0.05% of people in America actually financially contribute to poltiical campaigns, and thus exert exorbitant control over our political system. *How can we dive deeper into understanding the link between campaign funding sources and voting behavior? Can we use a model to predict an official's voting behavior and see how it differs from their stated/actual voting behavior?*

### Challenges

1. Extract Campaign Finance Data from [Cal-Access](http://cal-access.sos.ca.gov/Campaign/) and/or [SF Open Data](https://data.sfgov.org/City-Management-and-Ethics/Campaign-Finance-Database/sv2b-bdbj) and parse into a usable format (e.g. relational database). This will be very related, if not identical, to the work necessary to complete Problem Statement 1.
2. Find source of data for elected officials' voting behavior on bills in California. Then, extract this data and parse into a usable format (e.g. relational database)
    1. For example: https://www.couragescore.org/, although I'm not sure how reliable this specific one is
3. Build a predictive model that combines campaign finance data with voting records to see how tightly related funding sources are with voting behavior.
    1. This may eventually also include combining other sources of data (e.g. demographic data at the zip code level)
