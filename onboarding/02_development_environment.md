# Development Environment Setup
In this doc, we will go through things you need to install to get on the right "development environment" so that you can start contributing.

If you're on a Mac or PC you should be fine. The only caveat is that with PC, I would highly recommend using [Bash on ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) which provides a Linux environment without needing to spin up an entire Linux virtual machine! I also think working in a unix-like environment is great experience, especially in the tech world.

The following things that **must** be done are:

1. Installing Python and managing your python environment using conda
2. Clone the Repository
3. Connect to our database

Things that aren't absolutely necessary to start contributing, but I would still recommend doing are:

1. Installing Postgres locally

## Installing Python
We use Anaconda
https://www.continuum.io/downloads

You should download the Python 3 version.

## Setting Up Python Environment
Once you've installed Anaconda's distribution of Python, to clone and activate the appropriate python environment:

1. First `cd` into the root directory
2. `conda env create -f environment.yml`
    1. This clones the appropriate python environment which should be named `datasci-congressional-data`.
    2. See https://conda.io/docs/using/envs.html#use-environment-from-file for more information.
3. `source activate datasci-sba`
    1. This activates the conda python environment
    2. **Note you will need to activate the python environment every time you open a new terminal window** 
4. `pip install -r requirements.txt`
    1. Install all required Python Pacakges

A useful guide to conda environments: https://conda.io/docs/using/envs.html
The two important files are:
1. https://github.com/sfbrigade/datasci-sba/blob/master/environment.yml
2. https://github.com/sfbrigade/datasci-sba/blob/master/requirements.txt

## Clone the Repository
`git clone https://github.com/sfbrigade/datasci-congressional-data.git`

## Connecting to our database
In your ~/.bash_profile you need to set up environment variables corresponding to the database credentials. Slack the #university group for the appropriate credentials

The following below aren't absolutely necessary, but are pretty helpful.

## Installing Postgres locally
Installing postgres locally is technically optional, but will be really useful if you want to use `psql` command line tool. 

### For Mac
You can also install Postgres via HomeBrew: https://brew.sh/

`brew install postgres`

### For PC
To download Postgres: http://oscg-downloads.s3.amazonaws.com/packages/PostgreSQL-9.6.2-2-win64-bigsql.exe

For further instructions: https://medium.com/@colinrubbert/installing-ruby-on-rails-in-windows-10-w-bash-postgresql-e48e55954fbf

## Tech Stack

Here are the technologies used in the project, along with some tutorials if you'd like to learn.

| Tech | Version | Purpose | Getting Started |
|------|---------|---------|-----------------|
| Git | 2.4+ | Version control | [Udacity course](https://classroom.udacity.com/courses/ud775), [good comprehensive online book](https://git-scm.com/book/en/v2) |
| Postgres | 9.6 | Database | [Tutorial](https://www.postgresql.org/docs/8.0/static/tutorial.html) |
| SQL | |  Language used for database queries | [Tutorial from Postgres site](https://www.postgresql.org/docs/8.0/static/tutorial-sql.html) |
| Python | v3 | Data Analysis & Webserver | [Anaconda](https://www.continuum.io/downloads), [Python Language Tutorial](https://docs.python.org/3/tutorial/) |
| SciPy | | Python packages for data analysis | [Intro to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html), [NumPy Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) |
| Jupyter | | Easily share Python analysis with code and results | [Quickstart guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) |
| Django | 1.11.4 | Python webserver | Read the tutorial [here](https://docs.djangoproject.com/en/1.11/intro/), but install using `conda install django` |
| Javascript | ES2015 / ES6 | Clientside scripting language | [Tutorial covering modern JS](https://javascript.info/), [Quick reference of ES6 features](http://es6-features.org/) |
| Redux | 3.7.2 | Clientside state management | [Docs](http://redux.js.org/), [Good introductory videos](https://egghead.io/courses/getting-started-with-redux) |
| jQuery | 3.2.1 | Clientside DOM manipulation | [Tutorial](https://www.tutorialspoint.com/jquery/jquery-overview.htm) |

| Previous | Next |
|:---------|-----:|
| [Exploring the Data](./01_exploring_the_data.md) | [Tips and Tricks](./03_tips_and_tricks.md) |

