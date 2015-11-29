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

## Usage

While in a git repository, run `brag`

If you want to specify the date range to search in, use the `--start` and `--end` arguments (or `-s` and `-e` for short):

Example:

- `brag -s "one week ago" -e "yesterday"`
- `brag --start "2015-01-04"`
- `brag -s "2015-04-13" --end "two days ago"`

## Stability

To test the stability of this program I ran `brag` with no date-range arguments on the [django](https://github.com/django/django) repository.  At the time of testing, the repo had 1027 contributors.  Execution completed without errors, but it took 4m 46sec on my machine (Late 2013 MBP/i7/16GB RAM).

`brag` took 16sec to analyze Facebook's [flow](https://github.com/facebook/flow) repo with 99 contributors.

For Google's [googletest](https://github.com/google/googletest) repo with 20 contributors, it took 2sec.

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
