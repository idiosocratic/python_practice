#python cookbook practice 
'''long comment spanning lines
ends here'''


#Methods for text matching 
textmatching = 'this is my string'

print textmatching.startswith('this')

textmatching.endswith('ing')
 
import os

filenames_here = os.listdir('.')
 
print filenames_here 

print [name for name in filenames_here if name.startswith(('cook','hi'))] 

print any(name.endswith('.py') for name in filenames_here)

print [name.endswith('.py') for name in filenames_here]

# startswith method doesn't accept lists, only tuples or strings

mychoice = ['apple','pie','salad']

# convert mychoice
print tuple(mychoice)

choicestring = 'here is a pie'

print choicestring

print choicestring.endswith(tuple(mychoice))


# regular expression example
import re

url_1 = 'https://www.google.com'

print re.match('http:|https:',url_1)
