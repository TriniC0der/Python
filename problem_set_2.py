end = 6
count = 0 
for num in range(1,end+1):
	count += num
print count



'''
s = 'azcbobobegghakl'
name = 'bob'
counter = 0
for i in range(len(s)):

    for x in vowels:
        if s[i] == x:
            counter += 1
print "Number of times bob occurs is: %d" % counter
'''

# step 1 input next letter
# step 2 is it a B?
# 
# NO? goto step 1
# YES? add 1 to count goto step 3
# step 3 input next letter 
# is it a 0?
# NO? set count to 0  goto step 1 
# YES? add 1 to count goto step 4
# step 4 input next letter 
# is it a B?
# NO? set count to 0 goto step 1 
# YES? add count to bob set counter to 0
