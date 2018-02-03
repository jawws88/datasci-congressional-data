# Development Environment Setup
In this doc, we will go through things you need to install to get on the right "development environment" so that you can start contributing.

The instructions here mostly assume that you are working in a "Linux-like" environment. Without getting too much into the technical details, if you're using a Mac, then you should be fine without too much overhead.

If you're on a Windows, we highly recommend using [Bash on ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) which provides a Linux environment without needing to spin up an entire Linux virtual machine! (This will only work on Windows 10, if you're on a earlier version, we highly recommend upgrading to the latest version of Windows 10.) To install, follow the [installation guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10). I also think working in a unix-like environment is great experience, especially in the tech world.

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

## Clone the Repository
Before cloning the repository, we recommend you install Git Large File Storage. [Git Large File Storage](https://git-lfs.github.com/) is an open source Git extension for versioning large files. This can be a useful tool for storing large files using Git. This will be useful since we will be storing somewhat large source data files in our repository.

To install visit their [home page](https://git-lfs.github.com/) and/or view the installation [wiki instructions](https://github.com/git-lfs/git-lfs/wiki/Installation).

For example, on MAC OS, you will need to run the following. In addition, you may need to install [Home Brew](https://brew.sh/).

```
brew update
brew install git-lfs
git lfs install
```

Once you have installed Git Large File Storage, clone the repository by running one of the following in your terminal. We recommend using SSH since that'll allow you to push/pull without authenticating every time. If you don't already have your SSH keys set up see the instructions [here](https://help.github.com/articles/connecting-to-github-with-ssh/).

```
# If using HTTPS
git clone https://github.com/sfbrigade/datasci-congressional-data.git

# If using SSH
git clone git@github.com:sfbrigade/datasci-congressional-data.git
```

## Setting Up Python Environment
Once you've installed Anaconda's distribution of Python, to clone and activate the appropriate python environment:

1. First `cd` into the root directory
2. `conda env create -f environment.yml`
    1. This clones the appropriate python environment which should be named `datasci-congressional-data`.
    2. See https://conda.io/docs/using/envs.html#use-environment-from-file for more information.
3. `source activate datasci-congressional-data`
    1. This activates the conda python environment
    2. **Note you will need to activate the python environment every time you open a new terminal window** 
4. `conda env update -f environment.yml`
    1. In the future, if you need to update your environment run the above command.

For further information, here is a useful guide to conda environments: https://conda.io/docs/using/envs.html.

Note, the [environment.yml](../environment.yml) file must be kept up to date and is how we will ensure that every group member is on the same environment so any work we do on any machine is reproducible on any other machine.

## Connecting to our database
In your ~/.bash_profile you need to set up environment variables corresponding to the database credentials. Slack the #datasci-congressdata group for the appropriate credentials

### What is a .bash_profile and how do I add to it?
In short, a `~/.bash_profile` is a "hidden file" that is usually located in your home directory in your Linux environment. (`~` refers to the home directory, e.g. if you do `cd ~` you change directory into your home directory). This file is loaded before the Terminal loads your shell environment and contains all the startup configuration and preferences for your command line interface. For example, you can add environment variables, change the color of texts, and add aliases to functions you use on a frequent basis.

To add a line to your `~/.bash_profile`, you can use any text editor that you are familiar with (e.g. `emacs`, `vim`, `nano`). For those with limited experience working in Linux like environments a few quick Google Searches or asking your group members should work! Alternatively, you can also use something like the following to add directly into your `~/.bash_profile`:

```
echo "YOUR TEXT HERE" >> ~/.bash_profile
```

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
| PostgreSQL | |  Language used for database queries | [Tutorial from Postgres site](https://www.postgresql.org/docs/9.6/static/tutorial.html) |
| Python | v3 | Data Analysis & Webserver | [Anaconda](https://www.continuum.io/downloads), [Python Language Tutorial](https://docs.python.org/3/tutorial/) |
| Mode Analytics| | Online Application for SQL/Python Reporting and Analyses | [The SQL Tutorial for Data Analysis](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/)
| SciPy | | Python packages for data analysis | [Intro to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html), [NumPy Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) |
| Jupyter | | Easily share Python analysis with code and results | [Quickstart guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) |

As we move forward with the project, we will undoubtedly add Front End technologies as well. Add these in later!

| Previous | Next |
|:---------|-----:|
| [Exploring the Data](./01_exploring_the_data.md) | [Tips and Tricks](./03_tips_and_tricks.md) |

