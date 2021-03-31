def triengle(a):
	print(" "* (a-1) + "%%" +  " "*a)
	for i in range(2, a):
		print(" " * (a - i) + "%"*i + "%"*i + " "*(a - i))
	print("%"*(a*2))
print("--------------")
print("---TRIENGLE---")
print("--------------")
a = int(input("Enter the side of triengle: "))
triengle(a)
