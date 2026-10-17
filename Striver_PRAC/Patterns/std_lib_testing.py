import re
pattern=r'\d+'
text='there is 123 apple in 456'
match=(re.search(pattern,text))
print(match.group())