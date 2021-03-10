def magic(a):
  print("*"*a)
  print("*", end="")
  print(" "*(a-2), end="*\n")
  print("*"*a)
print("Magical square")
magic(int(input("Enter length")))
