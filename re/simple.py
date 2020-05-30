#!/usr/bin/python
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://jyo.com
https://youtube.com
https://www.yahoo.com
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#sub_urls = pattern.sub(r'\2\3', urls)

#print(sub_urls)

matches = pattern.findall(urls)

for match in matches:
    print(match)

#with open('data.txt', 'r') as f:
#    contents = f.read()
#    
#    matches = pattern.finditer(contents)
#    for match in matches:
#        print(match)












