x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

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
