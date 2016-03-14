#python cookbook practice 
'''long comment spanning lines
ends here'''


#Methods for text matching 
textmatching = 'this is my string'

print textmatching.startswith('this')

textmatching.endswith('ing')
 
import os

filenames_here = os.listdir('.')
 
print (filenames_here )

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

#Using any() with if:
eval_list = [True,False]

if any(eval_list):
  # do stuff 
  print 'yes'


# tuple unpacking
tup_1 = ('y','e','s')
y,e,s = tup_1

# String unpacking
str_1 = 'string'

a,b,c,d,e,f = str_1

# star unpacking

# *a,b = mychoice

print a


# DEQUE example

from collections import deque

def search(lines, pattern, history=5):
  previous_lines = deque(maxlen=history)
  for line in lines:
    if pattern in line: 
      yield line, previous_lines
    previous_lines.append(line)
    
#if __name__ == '__main__':
#  with open('somefile.txt') as f:
#    for line,prevlines in search(f,'python', 5):
#      for pline in prevlines:
#        print(pline, end='')
#      print(line, end='')
#      print('-'*20)

que_1 = deque(maxlen=3)
que_1.append(1)
que_1.append(2)
que_1.append(3)        

print que_1

que_1.append(4)

print que_1

que_1.appendleft(7)

que_1.pop()

print que_1

que_1.popleft()

print que_1

que_1.appendleft(13)

print que_1


# heapq module's nlargest, heapify & nsmallest

import heapq as hq

num_1 = [1,3,5,6,8,0,1,-23,46,27]

print(hq.nlargest(3,num_1))
print(hq.nsmallest(3,num_1))
print(hq.nlargest(3,num_1, key = lambda x: -x))
print(hq.nsmallest(3,num_1, key = lambda x: -x))

print num_1
hq.heapify(num_1)
print num_1

hq.heappop(num_1)
print num_1

# use ordereddict to preserve order in a dictionary

from collections import OrderedDict

dict_1 = OrderedDict()
dict_1['a'] = 1
dict_1['b'] = 2
dict_1['c'] = 3
dict_1['d'] = 4

for key in dict_1:
 print(key,dict_1[key])

# some zipping

zip_list1 = [1,3,5,7,9]
zip_list2 = [2,4,6,8,10]

lists_zip = zip(zip_list1,zip_list2)

print lists_zip

lists_zip_sorted = sorted(lists_zip, key = lambda x: -x[1])


# set operations on dicts

a = { 'aa': 1, 'ff': 2, 'tt': 6 }
b = { 'bb': 1, 'ff': 2, 'tt': 6, 'll': 9 }

print a.keys(), b.keys()

#a.keys() - b.keys()

#a.items() & b.items()

print a.items(), b.items()

dict_list = b.items()

for i in dict_list:
  print i
  


# using set() for deduping

list1 = [1,3,5,7,9,1,3,10,2,4,6,8,10]

  
def dedupe(items):

  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)    
     
      
list2 = list(dedupe(list1))      

print list1
print list2

# can only use generators once

lst_iter = dedupe(list1)

print lst_iter.next()

print lst_iter.next()

b = list(lst_iter)

print b

# slicing

list1 = [1,3,5,7,9,1,3,10,2,4,6,8,10]

sub_set = slice(3,7)
sub_set2 = slice(0,10,3)


sub_list = list1[sub_set]

sub_list2 = list1[sub_set2]

print list1
print sub_list
print sub_list2











    






































