# Task_05 Q_13:
# You are given an HTML code snippet of n lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.

# Print the detected items in the following format:
# Tag1
# Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Tag3
# -> Attribute3[0] > Attribute_value3[0]

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()