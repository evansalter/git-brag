[![Build Status](https://travis-ci.org/evansalter/git-brag.svg?branch=master)](https://travis-ci.org/evansalter/git-brag)

# Git Brag

A python script that prints out the contributions of each author in the project.  Statistics shown are:

- Files changed
- Lines inserted
- Lines deleted

## Requirements

- `git` command line tool must be installed
- Python version 2.7 (check with `python --version`)
- A UNIX OS such as Mac OS X or a Linux distro

## Installation

1. Clone the repository to the directory of your choosing
1. `cd git-brag`
1. `python setup.py install`

Note: If you do not have the privileges to install global packages, replace step 3 with `python setup.py install --user`.  The program will be installed in `~/.local/bin` on UNIX or `~/Library/Python/X.Y` on Mac.

## Usage

While in a git repository, run `brag`

If you want to specify the date range to search in, use the `--start` and `--end` arguments (or `-s` and `-e` for short):

Example:

- `brag -s "one week ago" -e "yesterday"`
- `brag --start "2015-01-04"`
- `brag -s "2015-04-13" --end "two days ago"`

## Testing

I have tested `brag` with a number of repos to ensure stability and to record speed.  I ran the following tests on my 2013 MacBook Pro (i7/16GB RAM/OS X 10.11).  All the tests completed successfully.

### Methodology

1. `git clone` repo and `cd` into it
2. Run `time brag` with no arguments.  This makes it report on every single commit since the creation of the repo
3. The total elapsed time is reported once the command completes

### Results

|Repository|Number of Contributors|Number of Commits|Running Time|
|---|---|---|
|[django](https://github.com/django)/[django](https://github.com/django/django)|1031|21,792|240.83sec (4min 1sec)|
|[facebook](https://github.com/facebook)/[flow](https://github.com/facebook/flow)|118|1,737|4.70sec|
|[google](https://github.com/google)/[googletest](https://github.com/google/googletest)|26|892|1.41sec|

For most projects, speed shouldn't be an issue.

Finally, for readability when running `brag` on large projects (>30 contributors) the graph will only include users that have contributed to at least 0.5% of the inserted lines.

## Demo

Running `brag` on the repo for the awesome Chrome extension “Terrorist to Coward” by [psiemens](https://github.com/psiemens) produces the following:

```
Peter Siemens:
Files changed: 9; Lines inserted: 77; Lines deleted: 16
---------------------------
Rob Cutmore:
Files changed: 1; Lines inserted: 7; Lines deleted: 0
---------------------------
Roman:
Files changed: 1; Lines inserted: 5; Lines deleted: 0
---------------------------
Spyros Panagiotopoulos:
Files changed: 2; Lines inserted: 13; Lines deleted: 0
---------------------------
Tianyun Shan:
Files changed: 2; Lines inserted: 4; Lines deleted: 2
---------------------------
filipdanic:
Files changed: 1; Lines inserted: 14; Lines deleted: 0
---------------------------
rgllm:
Files changed: 1; Lines inserted: 4; Lines deleted: 0
---------------------------

Totals:
Files changed: 17
Lines inserted: 124
Lines deleted: 18

Percentage of lines added per user:
[ # # # # # # # # # # # # # - - - - - - - ] 62%	--> Peter Siemens
[ # - - - - - - - - - - - - - - - - - - - ] 5%	--> Rob Cutmore
[ # - - - - - - - - - - - - - - - - - - - ] 4%	--> Roman
[ # # - - - - - - - - - - - - - - - - - - ] 10%	--> Spyros Panagiotopoulos
[ # - - - - - - - - - - - - - - - - - - - ] 3%	--> Tianyun Shan
[ # # # - - - - - - - - - - - - - - - - - ] 11%	--> filipdanic
[ # - - - - - - - - - - - - - - - - - - - ] 3%	--> rgllm
```

## TODO

- [x] ~~Allow date ranges to be passed as parameters~~
- [ ] Add support for charts showing files changed and lines deleted

If there is something else you would like added, let me know or submit a pull request.
