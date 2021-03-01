import random
a = []
b = int(input("Enter the length"))
for i in range(0, b):
  a.append(random.randint(12, 32))
for i in a:
  if i % 2 == 0:
    print(i, end = " ")
  else:
    print(i * 2, end=" ")
   
