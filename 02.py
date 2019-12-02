k = 0
for d in [1,0,1,0,0,0,0,0,1,1,0,0,0]:
  if d == 1:
   print(d, end ="")
   print()
   print("result1 = ",d)

print('ch result start')

for ch in [0,1,0,1,1,1,1,1,0,0,1,1,0]: 
 if ch == 1:
   print(ch, end ="")
   print()
   print("result2 = ",ch)

# or
# Если подключить модуль collections

from collections import Counter

сh = '0,1,0,1,1,1,1,1,0,0,1,1,0'
print(dict(Counter(ch)))

d = '1,0,1,0,0,0,0,0,1,1,0,0,0'
print(dict(Counter(d)))
