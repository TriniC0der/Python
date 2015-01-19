s = 'bobobobobobobobobobobobobob'
sub = "bob"
_start = 0
_end = 3
count = 0
bobs = 0

for x in s:
    count = s.count(sub,_start,_end)
    if count == 1:
        bobs += 1

    _start += 1
    _end += 1

print('Number of times bob occurs is: %d' % bobs)