# Tips and Tricks

## Working with Git and GitHub
Working with Git and GitHub might seem tricky at first, but I promise it gets much easier as you gain experience with it! Here are some basic instructions, but please feel free to ping the #university channel if you need help.

[Clone this repo locally](https://help.github.com/articles/cloning-a-repository/)
```
$ git clone https://github.com/sfbrigade/datasci-congressional-data.git
$ cd datasci-congressional-data
```
Create your own branch to start work:
```
$ git checkout -b <your-branch-name>
```
To change between branches: 
```
$ git checkout <branch-name>
```

Do some work:

For editing code, feel free to use whatever text editor you are comfortable with. However, we do recommend to use a **text editor** as opposed to a word processor (e.g. Microsoft Word) because a word processor will typically add markups which are not useful for code.

If you don't have an already preferred text editor, we recommend using [Sublime Text 3](https://www.sublimetext.com/3). You can download it for free with an "unlimited" trial period.

Once you've downloaded Sublime Text 3, it's usually helpful to be able to open Sublime Text 3 from the command line. This allows you to edit files much easier. To do this, add the following line to your `~/.bash_profile`:

```
alias subl='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
```

Then, to open a text file using Sublime from the command line, you can do:

```
$ subl <some-files>
```

When you're ready, commit, [merge any upstream changes](https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/), [deal with conflicts](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/), and push your branch
```
$ git add <edited-files>
$ git commit -m 'my awesome feature'
$ git push
```
[Create a Pull Request](https://help.github.com/articles/creating-a-pull-request/) from your pushed branch (compare branch) to the master branch

Another handy thing while working in terminal is to automatically show what branch you're working on in the command line. To do this, add the following your your `~/.bash_profile`

```
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```

## Using the Jupyter Notebook
To access the Jupyter notebook, type ```$ jupyter notebook``` on Mac or ```$ jupyter notebook --no-browser``` on Windows. It will say "The Jupyter terminal is running at http://localhost:8888/sometoken." Copy the link and paste it in your browser. 

If you have a Windows computer and are using Bash on Ubuntu on Windows, you may see an error message about a "dead kernel." [The fix](http://sdsawtelle.github.io/blog/output/bash-and-ipython-on-ubuntu-for-windows.html) is to type in Bash the following: ```$ conda install -c jzuhone zeromq=4.1.dev0```. To learn more about why this works, [click here.](http://sdsawtelle.github.io/blog/output/bash-and-ipython-on-ubuntu-for-windows.html)

## Querying tables in our database
See https://github.com/sfbrigade/datasci-congressional-data/blob/master/notebooks/query_sql_template.ipynb as an example to query tables in the database

## Educational Resources

- Git/GitHub - Free online course at Udacity: https://classroom.udacity.com/courses/ud775

- HTML and CSS - Free online course at Udacity: https://classroom.udacity.com/courses/ud304

- D3 Visualization Package - One-time free course at Rithm School (via meetup.com): https://www.meetup.com/meetup-code-your-face-off/events/241379532/

| Previous | Next |
|:---------| ----:|
| [Development Environment](./02_development_environment.md) | [Developing Locally](./04_developing_locally.md)|
