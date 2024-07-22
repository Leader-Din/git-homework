s = 'Sam this is a book'
list1 = s.split()
s2 =''

for w in list1:
    s2 +=(w[::-1]) + ''
print(s2)