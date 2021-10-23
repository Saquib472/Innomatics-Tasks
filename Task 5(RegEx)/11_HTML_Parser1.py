# Task_05 Q_11:
# You are given an HTML code snippet of n lines.
# Your task is to print start tags, end tags and empty tags separately.

# Format your results in the following way:
# Start : Tag1
# End   : Tag1
# Start : Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Start : Tag3
# -> Attribute3[0] > None
# Empty : Tag4
# -> Attribute4[0] > Attribute_value4[0]
# End   : Tag3
# End   : Tag2

import re
from html.parser import HTMLParser

class My_HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_endtag(self, tag):
        print("End".ljust(6) + ":", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

if __name__ == "__main__":
    parser = My_HTMLParser()
    n = int(input().strip())
    for _ in range(n):
        s = input()
        parser.feed(s)