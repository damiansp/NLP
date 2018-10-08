#! /bin/bash

tr -sc 'A-Za-z' '\n' < $1 | # one word per line
    tr A-Z a-z |            # all lower case
    sort |
    uniq -c |               # -c: count
    sort -nr                # -n: numerically, -r: reverse order
    
