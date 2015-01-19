from itertools import count

s = 'ffufibyuqobypjk'

def long_sub(input_string):
    maxsubstr = input_string[0:0] # empty slice (to accept subclasses of str)
    for start in range(len(input_string)): # O(n)
        for end in count(start + len(maxsubstr) + 1): # O(m)
            substr = input_string[start:end] # O(m)
            if len(substr) != (end - start): # found duplicates or EOS
                break
            if sorted(substr) == list(substr):
                maxsubstr = substr
    return maxsubstr

sub = (long_sub(s))
print "Longest substring in alphabetical order is: %s" %sub
