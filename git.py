# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:49:59 2021

@author: Martin


"""
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d['employees'][1]['lastName']='Smooth'

print(d)

#d['employees']['firstName']['Albert']='Bert'

a = [1, 2, 3] 
for i in a:
    print(f'Item {i} has index {a.index(i)}.')
    
mudu=[]
same=[5, 1, -10, 3, 3]
values=[5, 10, -10, 3, 5]
for i, j in enumerate(zip(same, values)):
    if j[0] == j[1]:
        mudu.append(i)
print(mudu)

print(enumerate(same))

class FunnyRange:

    def __getitem__(self, index):
        if index >= 10:
            raise IndexError
        return index

weird_sequence = FunnyRange()[5]
print(list(FunnyRange()))


def check_whitespace(lines):

    """Check for whitespace and line length issues."""

    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno+1, "\\r in line"
        if "\t" in line:
            yield lno+1, "OMG TABS!!!1"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno+1, "trailing whitespace"
        
    ###yield or return?
            
example1=[5, 1, -10, 3, 3]
example2=[5, 10, -10, 3, 5]
print([i for i,j in enumerate(zip(example1, example2)) if j[0] == j[1]])