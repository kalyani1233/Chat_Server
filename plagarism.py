import difflib
from difflib import SequenceMatcher
str1='i like pizza'
str2='i like tacos'

seq=SequenceMatcher(a=str1,b=str2)
print(seq.quick_ratio())