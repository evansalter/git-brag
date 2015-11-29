#!/usr/bin/env python

import subprocess
import os
import string

def convInt(s):
    try:
        return int(s)
    except ValueError:
        return 0

def zeroIfNull(s):
    if s.rstrip() == '':
        return "0"
    else:
        return s

def printGraph():
    print "Percentages of lines added per user:"
    for index in range(len(usernames)):
        percent = float(zeroIfNull(inserted[index]))/totalInserted*100
        print "[",
        numSigns=0
        for i in range(0, int(percent), 5):
            print "#",
            numSigns += 1
        for i in range(numSigns, 20, 1):
            print "-",
        print "] " + str(int(percent)) + "%\t--> " + usernames[index]

usernames = subprocess.check_output("git shortlog -s | cut -c8- | sort -u", shell=True).splitlines()

cmd1 = "git log --shortstat --author '"
cmd2 = "'| grep \"files\\? changed\" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print files, inserted, deleted}'"
# cmd2 = "' --since \"2015-10-30\" | grep \"files\\? changed\" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print files, inserted, deleted}'"

files = []
inserted = []
deleted = []

for index in range(len(usernames)):
    cmd = cmd1 + usernames[index] + cmd2
    print usernames[index] + ":"
    output = subprocess.check_output(cmd, shell=True)

    f = subprocess.check_output("echo \"" + output + "\" | cut -d ' ' -f1", shell=True).rstrip()
    i = subprocess.check_output("echo \"" + output + "\" | cut -d ' ' -f2", shell=True).rstrip()
    d = subprocess.check_output("echo \"" + output + "\" | cut -d ' ' -f3", shell=True).rstrip()
    files.append(f)
    inserted.append(i)
    deleted.append(d)

    print "Files changed: " + zeroIfNull(f) + "; Lines inserted: " + zeroIfNull(i) + "; Lines deleted: " + zeroIfNull(d)
    print "---------------------------"

totalFiles=0
totalInserted=0
totalDeleted=0

for index in range(len(files)):
    totalFiles += convInt(files[index])
    totalInserted += convInt(inserted[index])
    totalDeleted += convInt(deleted[index])

print "\nTotals:"
print "Files changed: " + str(totalFiles)
print "Lines inserted: " + str(totalInserted)
print "Lines deleted: " + str(totalDeleted)

print 

printGraph()
