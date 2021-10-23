# Task_05 Q_12:
# You are given an HTML code snippet of n lines.
# Your task is to print the single-line comments, multi-line comments and the data.

# Print the result in the following format:
# >>> Single-line Comment  
# Comment
# >>> Data                 
# My Data
# >>> Multi-line Comment  
# Comment_multiline[0]
# Comment_multiline[1]
# >>> Data
# My Data
# >>> Single-line Comment:  

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        print(comment)

    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()