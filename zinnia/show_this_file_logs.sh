#!/bin/bash
# Show the history of $1 file, from old to new
# Usage :    ./show_this_file_logs.sh views/archives.py

# In reverse order :
all_commits_code=$(git log $1 | grep commit | awk  '{print $2}' | awk '{a[i++]=$0} END {for (j=i-1; j>=0;) print a[j--] }')
for eachCommit in $all_commits_code
do
				git diff $eachCommit^ $eachCommit $1
				echo -e "\n\n------\n\n"
done
