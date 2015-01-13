
vowels = (['a', 'e', 'i', 'o', 'u'])
counter = 0
for i in range(len(s)):
    for x in vowels:
        if s[i] == x:
            counter += 1
print counter