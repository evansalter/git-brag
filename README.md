[![Build Status](https://travis-ci.org/evansalter/git-brag.svg?branch=master)](https://travis-ci.org/evansalter/git-brag)

# Git Brag

A python script that prints out the contributions of each author in the project.  Statistics shown are:

- Files changed
- Lines inserted
- Lines deleted

## Installation

1. Clone the repository to the directory of your choosing
1. `cd git-brag`
1. `python setup.py install`

## Usage

While in a git repository, run `brag`

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

- [ ] Allow date ranges to be passed as parameters
- [ ] Add support for charts showing files changed and lines deleted

If there is something else you would like added, let me know or submit a pull request.
