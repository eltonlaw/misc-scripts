""" Clean String

DESCRIPTION/CONTEXT
---------------------
Orginally, used to remove crap from an email that I got from Google.
Here's a small passage of that email:
'...<1t1a1b1l1e1 1c1l1a1s1s1=1'1s1i1t1e1s1-1l1a1y1o1u1t1-1n1a1m1e1-1o1n1e1-1c1'

Basically, the process was to...
    1) Copy email into string.txt
    2) Remove 1's
    3) Remove HTML tags

INPUT
-----
.txt file

OUTPUT
-----
None [Prints the cleaned string in console]


RUN
---
    >>> ls
    clean_string.py  string.txt
    >>> python3 clean_string.py string.txt
"""
import sys
import re


def clean(str_path):
    f = open(str_path)
    string = f.read()
    string = re.sub('1|<.*?>', "", string)
    return string


if __name__ == "__main__":
    path = "./" + sys.argv[1]
    print(clean(path))
